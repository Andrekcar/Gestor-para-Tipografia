"""
Ventana principal integrada con el .ui de Qt designer.

El id del pedido se guarda como dato oculto (Qt.UserRole) en la celda 0,
asi no necesita columna visible.
"""
import os
from datetime import date
from pathlib import Path

from PySide6.QtCore import Qt, QRectF, QRect, QStringListModel, QDate
from PySide6.QtGui import QIcon, QPainter, QColor, QPixmap, QTextCharFormat
from PySide6.QtWidgets import (
    QMainWindow, QTableWidgetItem, QHeaderView, QPushButton, QFileDialog,
    QStyledItemDelegate, QStyle, QComboBox, QSizePolicy, QCompleter,
    QDialog, QCalendarWidget, QVBoxLayout, QHBoxLayout, QLabel, QWidget,
    QLineEdit, QMessageBox
)

from app.models.pedido_repository import Pedido, PedidoRepository
from app.models.cliente_repository import ClienteRepository
from app.services.file_manager import copiar_plantilla
from app.views.clientes_main import ClientesPage
from app.views.ui.ui_main_window import Ui_MainWindow

# Ruta al icono de Corel dentro del proyecto
_COREL_ICON = Path(__file__).resolve().parents[2] / "app" / "assets" / "coreldraw.png"
_LOGO_GB    = Path(__file__).resolve().parents[2] / "app" / "assets" / "logo.png"

# Colores de los badges de estado (bg, fg)
_ESTADO_BADGE: dict[str, tuple[QColor, QColor]] = {
    "No Iniciado": (QColor(221, 240, 244), QColor(0, 0, 0, 178)),
    "En Progreso": (QColor(255, 243, 204), QColor(0, 0, 0, 178)),
    "Entregado":   (QColor(212, 245, 226), QColor(0, 0, 0, 178)),
}

class EstadoDelegate(QStyledItemDelegate):
    #Pinta la columna Estado como un badge redondeado con color de fondo
    def paint(self, painter: QPainter, option, index):
        painter.save()

def _combo_estado_qss(estado: str) -> str:
    #Genera el stylesheet del QComboBox de estado según el valor actual
    BG = {
        "No Iniciado": "rgb(221, 240, 244)",
        "En Progreso": "rgb(255, 243, 204)",
        "Entregado":   "rgb(212, 245, 226)",
    }
    bg = BG.get(estado, "rgb(255, 255, 255)")
    return f"QComboBox {{ background-color: {bg}; border: none; }}"

class _CalendarioRangoDialog(QDialog):
    """Modal con QCalendarWidget para elegir un rango de fechas.
    Primer click = fecha inicio
    Segundo click = fecha fin
    El botón Limpiar reinicia la selección."""

    _COLOR_EXTREMO = QColor(29, 140, 160)   
    _COLOR_RANGO   = QColor(212, 245, 226)

    def __init__(self, inicio: QDate | None, fin: QDate | None, parent=None):
        super().__init__(parent, Qt.WindowType.Popup)
        self.setWindowTitle("Seleccionar rango de fechas")
        self._inicio=inicio
        self._fin=fin
        self._esperando_fin=bool(inicio and not fin) #True si ya hay inicio y falta fin

        #Stylos para el calendario ya que este hereda de qt 
        self.setStyleSheet("""
            QDialog {
                background-color: #ffffff;
                border: 1px solid #d0d0d0;
            }
            QCalendarWidget {
                background-color: #ffffff;
                color: #1a1a1a;
            }
            QCalendarWidget QWidget#qt_calendar_navigationbar {
                background-color: #f0f0f0;
            }
            QCalendarWidget QToolButton {
                background-color: transparent;
                color: #1a1a1a;
                border: none;
            }
            QCalendarWidget QToolButton:hover {
                background-color: #e0e0e0;
                border-radius: 3px;
            }
            QCalendarWidget QMenu {
                background-color: #ffffff;
                color: #1a1a1a;
            }
            QCalendarWidget QSpinBox {
                background-color: #ffffff;
                color: #1a1a1a;
                border: 1px solid #d0d0d0;
            }
            QCalendarWidget QAbstractItemView {
                background-color: #ffffff;
                color: #1a1a1a;
                selection-background-color: #1d8ca0;
                selection-color: #ffffff;
                gridline-color: #e8e8e8;
            }
            QCalendarWidget QAbstractItemView:disabled {
                color: #b0b0b0;
            }
            QLabel {
                color: #1a1a1a;
                background-color: transparent;
            }
            QPushButton {
                background-color: #f0f0f0;
                color: #1a1a1a;
                border: 1px solid #d0d0d0;
                border-radius: 3px;
                padding: 4px 12px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
        """)

        lay = QVBoxLayout(self)
        lay.setContentsMargins(8, 8, 8, 8)
        lay.setSpacing(6)

        self._instruccion = QLabel()
        self._instruccion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lay.addWidget(self._instruccion)

        self._cal = QCalendarWidget()
        self._cal.setGridVisible(True)
        self._cal.clicked.connect(self._on_click_fecha)
        lay.addWidget(self._cal)

        btn_limpiar = QPushButton("Limpiar rango")
        btn_limpiar.clicked.connect(self._limpiar)
        lay.addWidget(btn_limpiar)

        self._actualizar_vista()

    # ── Slots internos ────────────────────────────────────────────────────────

    def _on_click_fecha(self, fecha: QDate):
        if not self._esperando_fin:
            # Primer click: establece inicio y espera el fin
            self._inicio = fecha
            self._fin    = None
            self._esperando_fin = True
        else:
            # Segundo click: establece fin (o reinicia si está antes del inicio)
            if fecha < self._inicio:
                self._inicio = fecha
                self._fin    = None
            else:
                self._fin = fecha
                self._esperando_fin = False
                self.accept()  # cierra el popup automáticamente al completar el rango
        self._actualizar_vista()

    def _limpiar(self):
        self._inicio = None
        self._fin    = None
        self._esperando_fin = False
        self._actualizar_vista()
        self.accept()

    # ── Helpers ───────────────────────────────────────────────────────────────

    def _actualizar_vista(self):
        """Actualiza la instrucción y el sombreado del calendario."""
        if not self._inicio:
            self._instruccion.setText("Selecciona la fecha de inicio")
        elif self._esperando_fin:
            self._instruccion.setText(
                f"Inicio: {self._inicio.toString('dd/MM/yyyy')} — selecciona la fecha de fin"
            )
        else:
            self._instruccion.setText(
                f"{self._inicio.toString('dd/MM/yyyy')} → {self._fin.toString('dd/MM/yyyy')}"
            )

        # Limpia todos los formatos previos
        self._cal.setDateTextFormat(QDate(), QTextCharFormat())

        if not self._inicio:
            return

        # Marca inicio
        fmt_ext = QTextCharFormat()
        fmt_ext.setBackground(self._COLOR_EXTREMO)
        fmt_ext.setForeground(QColor(255, 255, 255))
        self._cal.setDateTextFormat(self._inicio, fmt_ext)

        if self._fin:
            # Sombrea los días intermedios
            fmt_mid = QTextCharFormat()
            fmt_mid.setBackground(self._COLOR_RANGO)
            dia = self._inicio.addDays(1)
            while dia < self._fin:
                self._cal.setDateTextFormat(dia, fmt_mid)
                dia = dia.addDays(1)
            # Marca fin con el mismo color que el inicio
            self._cal.setDateTextFormat(self._fin, fmt_ext)

    @property
    def rango(self) -> tuple[QDate | None, QDate | None]:
        return self._inicio, self._fin

class DateRangeWidget(QWidget):
    """Widget para filtrar por rango de fechas.
    Muestra el rango seleccionado en una etiqueta y abre _CalendarioRangoDialog al hacer click."""

    _ESTILO = (
        "color: rgb(0,0,0); background-color: rgb(255,255,255);"
        "border: 1px solid rgba(1,1,1,50); padding: 0 8px; border-radius: 3px;"
    )

    def __init__(self, parent=None):
        super().__init__(parent)
        self._fecha_inicio: QDate | None = None
        self._fecha_fin:    QDate | None = None

        lay = QHBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(4)

        # Etiqueta que muestra el rango activo
        self._label = QLabel("Fecha: desde – hasta")
        self._label.setStyleSheet(self._ESTILO)
        self._label.setFixedHeight(41)
        self._label.setMinimumWidth(190)

        # Botón para abrir el calendario
        self._btn = QPushButton("📅")
        self._btn.setFixedSize(41, 41)
        
        self._btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self._btn.setToolTip("Seleccionar rango de fechas")
        self._btn.clicked.connect(self._abrir_calendario)

        lay.addWidget(self._label)
        lay.addWidget(self._btn)

    # ── Slot ──────────────────────────────────────────────────────────────────

    def _abrir_calendario(self):
        dlg = _CalendarioRangoDialog(self._fecha_inicio, self._fecha_fin, self)
        dlg.exec()
        self._fecha_inicio, self._fecha_fin = dlg.rango
        self._actualizar_label()

    # ── Helpers ───────────────────────────────────────────────────────────────

    def _actualizar_label(self):
        if self._fecha_inicio and self._fecha_fin:
            self._label.setText(
                f"{self._fecha_inicio.toString('dd/MM/yyyy')} – {self._fecha_fin.toString('dd/MM/yyyy')}"
            )
        elif self._fecha_inicio:
            self._label.setText(f"Desde {self._fecha_inicio.toString('dd/MM/yyyy')}")
        else:
            self._label.setText("Fecha: desde – hasta")

    # ── API pública ───────────────────────────────────────────────────────────

    @property
    def fecha_inicio(self) -> QDate | None:
        return self._fecha_inicio

    @property
    def fecha_fin(self) -> QDate | None:
        return self._fecha_fin

    def limpiar(self):
        self._fecha_inicio = None
        self._fecha_fin    = None
        self._actualizar_label()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Gestor de Tipografia")
        if _LOGO_GB.exists():
            self.setWindowIcon(QIcon(str(_LOGO_GB)))

        self._repo = PedidoRepository()
        self._repo_clientes = ClienteRepository()  # repositorio de clientes
        self._pedido_actual: Pedido | None = None
        self._estado_seleccionado = "No Iniciado"

        self._configurar_tabla()
        self._configurar_formulario()
        self._configurar_filtro()
        self._configurar_navegacion()
        self._connect_signals()
        self._refrescar_tabla()

    # ------------------------------------------------------------------
    # Configuracion inicial
    # ------------------------------------------------------------------

    def _configurar_formulario(self):
        estilo_input = "color: rgb(0, 0, 0); border: 1px solid rgba(1, 1, 1, 50);"

        self.lineCliente.hide()
        self.comboCliente = QComboBox(self.frame_detalle)
        self.comboCliente.setGeometry(QRect(30, 90, 291, 41))
        self.comboCliente.setEditable(True) # permite ingresar texto
        self.comboCliente.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.comboCliente.setStyleSheet(estilo_input)
        self.comboCliente.raise_()
        self.label_Cliente.raise_() 

        # QStringListModel exclusivo para el completer (no compartido con el combo).
        # El combo usa su propio modelo interno via addItems.
        self._modelo_clientes = QStringListModel(self)
        completer = QCompleter(self._modelo_clientes, self)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self.comboCliente.setCompleter(completer)

        self._cargar_clientes_combo() # carga inicial de nombres desde la BD

        self.lineTrabajo.setStyleSheet(estilo_input)
        self.linePlantilla.setStyleSheet(estilo_input)
        self.linePlantilla.setReadOnly(True)
        self.linePlantilla.setPlaceholderText("Selecciona un archivo .cdr...")
        self.plainTextDescripcion.setStyleSheet(estilo_input)
        self.pushButton_2.setText("...")
        self.pushButton_2.setToolTip("Seleccionar archivo de plantilla (.cdr)")
        self.pushButton_2.setCursor(Qt.CursorShape.PointingHandCursor) # Cambia el cursor
        self.pushButton_2.setStyleSheet("""
            QPushButton {
                background-color: rgb(29, 140, 160);
                color: white;
                border-radius: 1px;
                font: bold 11pt "Segoe UI";
            }
            QPushButton:hover { background-color: rgb(20, 110, 130); }
        """)

        if _LOGO_GB.exists():
            self.label_logogb.setPixmap(QPixmap(str(_LOGO_GB)))

        self._configurar_badges_estado()

    def _configurar_filtro(self):
        """Configura panel de filtro:
        - Completer en comboBoxCliente para buscar por subcadena
        - Reemplaza frame_fecha_rango por DateRangeWidget"""

        # Completer para el combo de cliente en el filtro
        completer_filtro = QCompleter(self._modelo_clientes, self)
        completer_filtro.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer_filtro.setFilterMode(Qt.MatchFlag.MatchContains)
        self.comboBoxCliente.setCompleter(completer_filtro)

        # Sustituye el placeholder frame_fecha_rango por el widget de rango de fechas
        layout_filtro = self.frameFiltro.layout()
        idx = layout_filtro.indexOf(self.frame_fecha_rango)
        layout_filtro.removeWidget(self.frame_fecha_rango)
        self.frame_fecha_rango.deleteLater()

        self._date_range = DateRangeWidget(self)
        layout_filtro.insertWidget(idx, self._date_range)

    _BADGE_BASE = {
        "No Iniciado": ("rgb(221,240,244)", "rgb(190,225,233)"),
        "En Progreso": ("rgb(255,243,204)", "rgb(230,210,140)"),
        "Entregado":   ("rgb(212,245,226)", "rgb(160,220,190)"),
    }

    def _configurar_badges_estado(self):
        #Hace los tres chips de estado clickeables
        badges = [
            (self.lineNo_iniciado, "No Iniciado"),
            (self.lineEn_progreso, "En Progreso"),
            (self.lineEntregado, "Entregado"),
        ]
        for widget, estado in badges:
            widget.setReadOnly(True) # para que no se pueda editar el texto
            widget.setCursor(Qt.CursorShape.PointingHandCursor) 
            # Al hacer click, se llama a _seleccionar_badge con el estado correspondiente
            widget.mousePressEvent = lambda _, s=estado: self._seleccionar_badge(s) 
        # Al iniciar, seleccionamos "No Iniciado" por defecto
        self._seleccionar_badge("No Iniciado")

    def _cargar_clientes_combo(self):
        """Recarga la lista de clientes en el combo del formulario, en el del filtro
        y en el completer compartido"""
        
        nombres = [c.nombre for c in self._repo_clientes.get_all()]

        # Modelo compartido actualiza autocompletado en formulario y filtro a la vez
        self._modelo_clientes.setStringList(nombres)

        # Combo del formulario
        texto_actual = self.comboCliente.currentText()
        self.comboCliente.blockSignals(True)
        self.comboCliente.clear()
        self.comboCliente.addItems(nombres)
        self.comboCliente.setCurrentIndex(-1)
        self.comboCliente.blockSignals(False)
        if texto_actual:
            self.comboCliente.setCurrentText(texto_actual)

        # Combo del filtro
        texto_filtro = self.comboBoxCliente.currentText()
        self.comboBoxCliente.blockSignals(True)
        self.comboBoxCliente.clear()
        self.comboBoxCliente.addItem("") # opción vacía = "todos"
        self.comboBoxCliente.addItems(nombres)
        self.comboBoxCliente.setCurrentIndex(0)
        self.comboBoxCliente.blockSignals(False)
        if texto_filtro:
            self.comboBoxCliente.setCurrentText(texto_filtro)

    def _seleccionar_badge(self, estado: str):
        #Resalta el badge activo
        self._estado_seleccionado = estado
        pares = [
            (self.lineNo_iniciado, "No Iniciado"),
            (self.lineEn_progreso, "En Progreso"),
            (self.lineEntregado, "Entregado"),
        ]
        for widget, nombre in pares:
            bg, borde_color = self._BADGE_BASE.get(nombre, ("rgb(290,220,220)", "rgb(180,180,180)")) 
            if nombre == estado:
                widget.setStyleSheet(
                    f"color: rgba(0,0,0,0.85); font: 700 9pt 'Segoe UI';"
                    f"border-radius: 15px; background-color: {bg};"
                    f"border: 2px solid {borde_color};"
                )
            else:
                widget.setStyleSheet(
                    f"color: rgba(0,0,0,0.35); font: 700 9pt 'Segoe UI';"
                    f"border-radius: 15px; background-color: {bg};"
                    f"border: 1px solid transparent;"
                )

    def _configurar_navegacion(self):
        self._clientes_page = ClientesPage()
        self.horizontalLayout_3.addWidget(self._clientes_page)
        self._clientes_page.hide() # empieza oculta, pedidos es la vista inicial
        self.toolButtonPedidos.clicked.connect(self._mostrar_pedidos)
        self.toolButtonClientes.clicked.connect(self._mostrar_clientes)

    def _mostrar_pedidos(self):
        #Politicas para forzar y expandir la tabla pedidos en frame  
        _exp = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding) 
        _ign = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        
        self._clientes_page.setSizePolicy(_ign)
        self._clientes_page.hide()
        self.frame_pedidos.setSizePolicy(_exp)
        self.frame_pedidos.show()
        self.frame_detalle.setSizePolicy(_exp)
        self.frame_detalle.show()
        self.labelTitulo.setText("Gestor de Pedidos")
        self._cargar_clientes_combo()  # refresca la lista

    def _mostrar_clientes(self):
        #Politicas para forzar y expandir la tabla pedidos en frame  
        _exp = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        _ign = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        
        self.frame_pedidos.setSizePolicy(_ign)
        self.frame_pedidos.hide()
        self.frame_detalle.setSizePolicy(_ign)
        self.frame_detalle.hide()
        self._clientes_page.setSizePolicy(_exp)
        self._clientes_page.show()
        self.labelTitulo.setText("Clientes")

    def _configurar_tabla(self):
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # Und (2) pequeña, Estado (3) y Plantilla (6) con ancho fijo
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)
        self.tableWidget.setColumnWidth(2, 50)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)
        self.tableWidget.setColumnWidth(3, 130)
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.Fixed)
        self.tableWidget.setColumnWidth(6, 110)
        self.tableWidget.setSelectionBehavior(
            self.tableWidget.SelectionBehavior.SelectRows
        )
        self.tableWidget.setEditTriggers(
            self.tableWidget.EditTrigger.NoEditTriggers
        )
        self.tableWidget.verticalHeader().setDefaultSectionSize(35)
        # Delegate para pintar los badges de estado
        self.tableWidget.setItemDelegateForColumn(3, EstadoDelegate(self.tableWidget))

    # ------------------------------------------------------------------
    # Conexion de señales
    # ------------------------------------------------------------------

    def _connect_signals(self):
        self.toolButtonAdd.clicked.connect(self._on_nuevo_pedido)
        self.toolButtonGuardar.clicked.connect(self._on_guardar)
        self.toolButtonEliminar.clicked.connect(self._on_eliminar)
        self.toolButtonBuscar.clicked.connect(self._on_buscar)
        self.lineEditTrabajo.returnPressed.connect(self._on_buscar) # busca al presionar Enter
        self.pushButton_2.clicked.connect(self._on_elegir_plantilla)
        self.tableWidget.itemSelectionChanged.connect(self._on_seleccion_cambiada)

    # ------------------------------------------------------------------
    # Slots
    # ------------------------------------------------------------------

    def _on_nuevo_pedido(self):
        self._pedido_actual = None
        self.comboCliente.clearEditText() # limpia el texto sin borrar la lista de opciones
        self.comboCliente.setCurrentIndex(-1)
        self.lineTrabajo.clear()
        self.plainTextDescripcion.clear()
        self.spinBoxUnd.setValue(1)
        self.linePlantilla.clear()
        self.label_Orden.setText("Nuevo Pedido")
        self._seleccionar_badge("No Iniciado")
        self.tableWidget.clearSelection() #

    def _on_elegir_plantilla(self):
        #Abre un selector de archivo para elegir la plantilla .cdr
        ruta, _ = QFileDialog.getOpenFileName( 
            self,
            "Seleccionar plantilla de Corel Draw",
            "",
            "Corel Draw (*.cdr);;Todos los archivos (*)",
        )
        if ruta:
            self.linePlantilla.setText(ruta)

    def _on_guardar(self):
        cliente = self.comboCliente.currentText().strip() # funciona tanto si eligió de la lista como si escribió
        tipo = self.lineTrabajo.text().strip()
        descripcion = self.plainTextDescripcion.toPlainText().strip()
        plantilla = self.linePlantilla.text().strip()
        estado = self._estado_seleccionado
        unidades = self.spinBoxUnd.value()

        if not cliente:
            self.statusBar().showMessage("El campo Cliente es obligatorio.", 3000)
            return

        # Copia la plantilla a {Docs}/{cliente}/{año}/{cliente}_{tipo}_{fecha}.cdr
        # Si la base es más reciente que la copia existente se actualiza 
        if plantilla and cliente:
            copia = copiar_plantilla(
                cliente,
                plantilla,
                tipo_trabajo=tipo,
                fecha=date.today().strftime("%Y%m%d"),
            )
            if copia:
                plantilla = str(copia)
                self.linePlantilla.setText(plantilla)

        if self._pedido_actual is not None:
            self._pedido_actual.cliente = cliente
            self._pedido_actual.tipo_trabajo = tipo
            self._pedido_actual.descripcion = descripcion
            self._pedido_actual.estado = estado
            self._pedido_actual.plantilla = plantilla
            self._pedido_actual.unidades = unidades
            self._repo.update(self._pedido_actual)
            self.statusBar().showMessage("Pedido actualizado.", 3000)
        else:
            pedido = Pedido(
                cliente=cliente,
                tipo_trabajo=tipo,
                descripcion=descripcion,
                estado=estado,
                plantilla=plantilla,
                unidades=unidades,
                fecha_solicitud=date.today().isoformat(),
            )
            self._repo.insert(pedido)
            self._on_nuevo_pedido() # limpia el formulario tras guardar
            self.statusBar().showMessage(f'Pedido de "{tipo}" agregado.', 3000)
            

        self._cargar_clientes_combo()
        # refresca la lista por si se registró un cliente nuevo
        self._refrescar_tabla()

    def _on_eliminar(self):
        if self._pedido_actual is None:
            self.statusBar().showMessage("Selecciona un pedido para eliminar.", 3000)
            return
        respuesta = QMessageBox.question(
            self, "Eliminar pedido",
            f"¿Eliminar el pedido de {self._pedido_actual.cliente}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if respuesta != QMessageBox.StandardButton.Yes:
            return
        self._repo.delete(self._pedido_actual.id)
        nombre = self._pedido_actual.cliente
        self._pedido_actual = None
        self.label_Orden.setText("Orden ID-01")
        self._refrescar_tabla()
        self.statusBar().showMessage(f'Pedido "{nombre}" eliminado.', 3000)

    def _on_buscar(self):
        """Filtra las filas de la tabla según los controles del panel de filtro

        Regla de entregados: por defecto están ocultos
        En cuanto el usuario activa cualquier filtro, los entregados que coincidan
        se vuelven visibles — de lo contrario se mantienen ocultos."""
        cliente = self.comboBoxCliente.currentText().strip().lower()
        tipo    = self.lineEditTrabajo.text().strip().lower()
        estado  = self.comboBoxEstado.currentText().strip()
        f_ini   = self._date_range.fecha_inicio 
        f_fin   = self._date_range.fecha_fin     

        # Si no hay ningún filtro activo, restaura la vista por defecto
        # (entregados ocultos, resto visibles)
        hay_filtro = bool(cliente or tipo or (estado and estado != "Todos") or f_ini or f_fin)
        if not hay_filtro:
            self._refrescar_tabla()
            return

        for row in range(self.tableWidget.rowCount()):
            visible = True

            # Filtro cliente (col 0 — QTableWidgetItem)
            if cliente:
                item = self.tableWidget.item(row, 0)
                if not item or cliente not in item.text().lower():
                    visible = False

            # Filtro tipo de trabajo (col 1)
            if visible and tipo:
                item = self.tableWidget.item(row, 1)
                if not item or tipo not in item.text().lower():
                    visible = False

            # Filtro estado (col 3 — QComboBox widget incrustado)
            if visible and estado and estado != "Todos":
                widget = self.tableWidget.cellWidget(row, 3)
                if not widget or widget.currentText() != estado:
                    visible = False

            # Filtro rango de fechas sobre fecha_solicitud (col 4, formato yyyy-MM-dd)
            if visible and (f_ini or f_fin):
                item = self.tableWidget.item(row, 4)
                if item and item.text():
                    fecha_row = QDate.fromString(item.text(), "yyyy-MM-dd")
                    if f_ini and fecha_row < f_ini:
                        visible = False
                    if f_fin and fecha_row > f_fin:
                        visible = False

            self.tableWidget.setRowHidden(row, not visible)

    def _on_seleccion_cambiada(self): #Carga los datos de la seleccion en tabla
        row = self.tableWidget.currentRow()
        if row < 0:
            return
        celda_cliente = self.tableWidget.item(row, 0) 
        if celda_cliente is None:
            return
        pedido_id = celda_cliente.data(Qt.ItemDataRole.UserRole) 
        self._pedido_actual = self._repo.get_by_id(pedido_id)
        if self._pedido_actual is None:
            return

        self.label_Orden.setText(f"Orden ID-{self._pedido_actual.id}")
        self.comboCliente.setCurrentText(self._pedido_actual.cliente)
        self.lineTrabajo.setText(self._pedido_actual.tipo_trabajo)
        self.plainTextDescripcion.setPlainText(self._pedido_actual.descripcion)
        self.spinBoxUnd.setValue(self._pedido_actual.unidades)
        self.linePlantilla.setText(self._pedido_actual.plantilla)
        self._seleccionar_badge(self._pedido_actual.estado)

    def _on_abrir_plantilla(self, ruta: str):
        #Abre el archivo .cdr
        if not ruta:
            self.statusBar().showMessage("Este pedido no tiene plantilla asignada.", 3000)
            return
        if not os.path.exists(ruta):
            self.statusBar().showMessage(f"Archivo no encontrado: {ruta}", 4000)
            return
        os.startfile(ruta)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _crear_combo_estado(self, pedido_id: int, estado: str) -> QComboBox:
        #QComboBox estilizado como badge para la columna Estado de la tabla."""
        combo = QComboBox()
        combo.addItems(["No Iniciado", "En Progreso", "Entregado"])
        combo.setCurrentText(estado)
        combo.setStyleSheet(_combo_estado_qss(estado))
  
        def _on_cambio(nuevo: str):
            combo.setStyleSheet(_combo_estado_qss(nuevo))
            pedido = self._repo.get_by_id(pedido_id)
            if pedido:
                pedido.estado = nuevo
                # Logica para capturar la hora de entrega segun estado
                if nuevo == "Entregado" and not pedido.fecha_entrega:
                    pedido.fecha_entrega = date.today().isoformat()
                self._repo.update(pedido)
                self._refrescar_tabla()
  
            if self._pedido_actual and self._pedido_actual.id == pedido_id:
                self._pedido_actual.estado = nuevo
                self._seleccionar_badge(nuevo)
                self._refrescar_tabla()
                
        combo.currentTextChanged.connect(_on_cambio)
        return combo

    def _crear_boton_plantilla(self, ruta: str, estado: str = "") -> QPushButton:
        #Crea el boton con logo de Corel para la columna Plantilla
        _BG = {
            "No Iniciado": "#ddf0f4",
            "En Progreso": "#fff3cc",
            "Entregado": "#d4f5e2",
        }
        bg = _BG.get(estado, "#ffffff")

        btn = QPushButton()
        btn.setToolTip(ruta if ruta else "Sin plantilla asignada")
        btn.setCursor(Qt.CursorShape.PointingHandCursor)

        if _COREL_ICON.exists():
            btn.setIcon(QIcon(str(_COREL_ICON)))

        if ruta:
            btn.setStyleSheet(f"""
                QPushButton {{
                    border: none;
                    text-align: center;
                    background-color: {bg};
                }}
                QPushButton:hover {{ background-color: #96b7a2; }}
            """)
            btn.clicked.connect(lambda: self._on_abrir_plantilla(ruta))
        else:
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {bg};
                    border: none;
                }}
            """)
            btn.setEnabled(False)

        return btn

    _COLORES_ESTADO = {
        "No Iniciado": QColor(221, 240, 244),
        "En Progreso": QColor(255, 243, 204),
        "Entregado":   QColor(212, 245, 226),
    }

    def _refrescar_tabla(self):
        #Recarga todos los pedidos desde la BD y repinta la tabla
        pedidos = self._repo.get_all()
        self.tableWidget.setRowCount(0)
        for pedido in pedidos:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)

            item_cliente = QTableWidgetItem(pedido.cliente)
            item_cliente.setData(Qt.ItemDataRole.UserRole, pedido.id)
            self.tableWidget.setItem(row, 0, item_cliente)

            self.tableWidget.setItem(row, 1, QTableWidgetItem(pedido.tipo_trabajo))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(pedido.unidades)))
            combo = self._crear_combo_estado(pedido.id, pedido.estado)
            self.tableWidget.setCellWidget(row, 3, combo)
            self.tableWidget.setItem(row, 4, QTableWidgetItem(pedido.fecha_solicitud))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(pedido.fecha_entrega))

            btn = self._crear_boton_plantilla(pedido.plantilla, pedido.estado)
            self.tableWidget.setCellWidget(row, 6, btn)

            self.tableWidget.setItem(row, 7, QTableWidgetItem(""))

            color = self._COLORES_ESTADO.get(pedido.estado, QColor(255, 255, 255))
            for col in [0, 1, 2, 4, 5, 7]:
                item = self.tableWidget.item(row, col)
                if item:
                    item.setBackground(color)

            # Oculta por defecto los pedidos entregados; se revelan filtrando por estado
            if pedido.estado == "Entregado":
                self.tableWidget.setRowHidden(row, True)

