"""
Ventana principal integrada con el .ui de Qt Creator.

Columnas actuales de tableWidget (7):
  0=Cliente  1=Tipo de Trabajo  2=Estado  3=Fecha Solicitud
  4=Fecha Entrega  5=Plantilla 

El id del pedido se guarda como dato oculto (Qt.UserRole) en la celda 0,
asi no necesita columna visible.
"""
import os
from datetime import date
from pathlib import Path

from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QIcon, QPainter, QColor
from PySide6.QtWidgets import (
    QMainWindow, QTableWidgetItem, QHeaderView, QPushButton, QFileDialog,
    QStyledItemDelegate, QStyle, QComboBox, QSizePolicy
)

from app.models.pedido_repository import Pedido, PedidoRepository
from app.views.clientes_page import ClientesPage
from app.views.ui.ui_main_window import Ui_MainWindow

# Ruta al icono de Corel dentro del proyecto
_COREL_ICON = Path(__file__).resolve().parents[2] / "app" / "assets" / "coreldraw.png"

# Colores de los badges de estado (bg, fg)
_ESTADO_BADGE: dict[str, tuple[QColor, QColor]] = {
    "No Iniciado": (QColor(221, 240, 244), QColor(0, 0, 0, 178)),
    "En Progreso": (QColor(255, 243, 204), QColor(0, 0, 0, 178)),
    "Entregado":   (QColor(212, 245, 226), QColor(0, 0, 0, 178)),
}

class EstadoDelegate(QStyledItemDelegate):
    """Pinta la columna Estado como un badge redondeado con color de fondo."""
    def paint(self, painter: QPainter, option, index):
        painter.save()

def _combo_estado_qss(estado: str) -> str:
    """Genera el stylesheet del QComboBox de estado según el valor actual."""
    BG = {
        "No Iniciado": "rgb(221, 240, 244)",
        "En Progreso": "rgb(255, 243, 204)",
        "Entregado":   "rgb(212, 245, 226)",
    }

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self._repo = PedidoRepository()
        self._pedido_actual: Pedido | None = None
        self._estado_seleccionado = "No Iniciado"

        self._configurar_tabla()
        self._configurar_formulario()
        self._configurar_navegacion()
        self._connect_signals()
        self._refrescar_tabla()

    # ------------------------------------------------------------------
    # Configuracion inicial
    # ------------------------------------------------------------------

    def _configurar_formulario(self):
        estilo_input = "color: rgb(0, 0, 0); border: 1px solid rgba(1, 1, 1, 50);"
        self.lineCliente.setStyleSheet(estilo_input)
        self.lineTrabajo.setStyleSheet(estilo_input)
        self.linePlantilla.setStyleSheet(estilo_input)
        self.linePlantilla.setReadOnly(True)
        self.linePlantilla.setPlaceholderText("Selecciona un archivo .cdr...")
        self.plainTextDescripcion.setStyleSheet(estilo_input)
        self.pushButton_2.setText("...")
        self.pushButton_2.setToolTip("Seleccionar archivo de plantilla (.cdr)")
        self.pushButton_2.setCursor(Qt.CursorShape.PointingHandCursor)
        self.pushButton_2.setStyleSheet("""
            QPushButton {
                background-color: rgb(29, 140, 160);
                color: white;
                border-radius: 1px;
                font: bold 11pt "Segoe UI";
            }
            QPushButton:hover { background-color: rgb(20, 110, 130); }
        """)

        self._configurar_badges_estado()

    _BADGE_BASE = {
        "No Iniciado": ("rgb(221,240,244)", "rgb(190,225,233)"),
        "En Progreso": ("rgb(255,243,204)", "rgb(230,210,140)"),
        "Entregado":   ("rgb(212,245,226)", "rgb(160,220,190)"),
    }

    def _configurar_badges_estado(self):
        """Hace los tres chips de estado clickeables como radio-buttons."""
        badges = [
            (self.lineNo_iniciado, "No Iniciado"),
            (self.lineEn_progreso, "En Progreso"),
            (self.lineEntregado,   "Entregado"),
        ]
        for widget, estado in badges:
            widget.setReadOnly(True) # para que no se pueda editar el texto
            widget.setCursor(Qt.CursorShape.PointingHandCursor) 
            # Al hacer click, se llama a _seleccionar_badge con el estado correspondiente
            widget.mousePressEvent = lambda _, s=estado: self._seleccionar_badge(s) 
        # Al iniciar, seleccionamos "No Iniciado" por defecto
        self._seleccionar_badge("No Iniciado")

    def _seleccionar_badge(self, estado: str):
        """Resalta el badge activo y apaga los demás."""
        self._estado_seleccionado = estado
        pares = [
            (self.lineNo_iniciado, "No Iniciado"),
            (self.lineEn_progreso, "En Progreso"),
            (self.lineEntregado,   "Entregado"),
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
        self._clientes_page.hide()   # empieza oculta, pedidos es la vista inicial
        self.toolButtonPedidos.clicked.connect(self._mostrar_pedidos)
        self.toolButtonClientes.clicked.connect(self._mostrar_clientes)

    def _mostrar_pedidos(self):
        _exp = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        _ign = QSizePolicy(QSizePolicy.Policy.Ignored,   QSizePolicy.Policy.Ignored)
        self._clientes_page.setSizePolicy(_ign)
        self._clientes_page.hide()
        self.frame_pedidos.setSizePolicy(_exp)
        self.frame_pedidos.show()
        self.frame_detalle.setSizePolicy(_exp)
        self.frame_detalle.show()
        self.labelTitulo.setText("Gestor de Pedidos")

    def _mostrar_clientes(self):
        _exp = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        _ign = QSizePolicy(QSizePolicy.Policy.Ignored,   QSizePolicy.Policy.Ignored)
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
        # Columna Estado (2) y Plantilla (5) con ancho fijo
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)
        self.tableWidget.setColumnWidth(2, 130)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.Fixed)
        self.tableWidget.setColumnWidth(5, 110)
        self.tableWidget.setSelectionBehavior(
            self.tableWidget.SelectionBehavior.SelectRows
        )
        self.tableWidget.setEditTriggers(
            self.tableWidget.EditTrigger.NoEditTriggers
        )
        self.tableWidget.verticalHeader().setDefaultSectionSize(35)
        # Delegate para pintar los badges de estado
        self.tableWidget.setItemDelegateForColumn(2, EstadoDelegate(self.tableWidget))

    # ------------------------------------------------------------------
    # Conexion de señales
    # ------------------------------------------------------------------

    def _connect_signals(self):
        self.toolButtonAdd.clicked.connect(self._on_nuevo_pedido)
        self.toolButtonGuardar.clicked.connect(self._on_guardar)
        self.toolButtonEliminar.clicked.connect(self._on_eliminar)
        self.toolButtonBuscar.clicked.connect(self._on_buscar)
        self.pushButton_2.clicked.connect(self._on_elegir_plantilla)
        self.tableWidget.itemSelectionChanged.connect(self._on_seleccion_cambiada)

    # ------------------------------------------------------------------
    # Slots
    # ------------------------------------------------------------------

    def _on_nuevo_pedido(self):
        self._pedido_actual = None
        self.lineCliente.clear()
        self.lineTrabajo.clear()
        self.plainTextDescripcion.clear()
        self.linePlantilla.clear()
        self.label_Orden.setText("Nuevo Pedido")
        self._seleccionar_badge("No Iniciado")
        self.tableWidget.clearSelection() #

    def _on_elegir_plantilla(self):
        """Abre un selector de archivo para elegir la plantilla .cdr."""
        ruta, _ = QFileDialog.getOpenFileName( 
            self,
            "Seleccionar plantilla de Corel Draw",
            "",
            "Corel Draw (*.cdr);;Todos los archivos (*)",
        )
        if ruta:
            self.linePlantilla.setText(ruta)

    def _on_guardar(self):
        cliente = self.lineCliente.text().strip() 
        tipo = self.lineTrabajo.text().strip()
        descripcion = self.plainTextDescripcion.toPlainText().strip() 
        plantilla = self.linePlantilla.text().strip()
        estado = self._estado_seleccionado

        if not cliente:
            self.statusBar().showMessage("El campo Cliente es obligatorio.", 3000)
            return

        if self._pedido_actual is not None:
            self._pedido_actual.cliente = cliente
            self._pedido_actual.tipo_trabajo = tipo
            self._pedido_actual.descripcion = descripcion
            self._pedido_actual.estado = estado
            self._pedido_actual.plantilla = plantilla
            self._repo.update(self._pedido_actual)
            self.statusBar().showMessage("Pedido actualizado.", 3000)
        else:
            pedido = Pedido(
                cliente=cliente,
                tipo_trabajo=tipo,
                descripcion=descripcion,
                estado=estado,
                plantilla=plantilla,
                fecha_solicitud=date.today().isoformat(),
            )
            self._repo.insert(pedido)
            self.statusBar().showMessage(f'Pedido de"{tipo}" agregado.', 3000)

        self._refrescar_tabla()

    def _on_eliminar(self):
        if self._pedido_actual is None:
            self.statusBar().showMessage("Selecciona un pedido para eliminar.", 3000)
            return
        self._repo.delete(self._pedido_actual.id)
        nombre = self._pedido_actual.cliente
        self._pedido_actual = None
        self.label_Orden.setText("Orden ID-01")
        self._refrescar_tabla()
        self.statusBar().showMessage(f'Pedido "{nombre}" eliminado.', 3000)

    def _on_buscar(self):
        pass

    def _on_seleccion_cambiada(self): # 
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
        self.lineCliente.setText(self._pedido_actual.cliente)
        self.lineTrabajo.setText(self._pedido_actual.tipo_trabajo)
        self.plainTextDescripcion.setPlainText(self._pedido_actual.descripcion)
        self.linePlantilla.setText(self._pedido_actual.plantilla)
        self._seleccionar_badge(self._pedido_actual.estado)

    def _on_abrir_plantilla(self, ruta: str):
        """Abre el archivo .cdr con la aplicacion predeterminada del sistema."""
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
        """QComboBox estilizado como badge para la columna Estado de la tabla."""
        combo = QComboBox()
        combo.addItems(["No Iniciado", "En Progreso", "Entregado"])
        combo.setCurrentText(estado) # selecciona el estado actual del pedido
  
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

    def _crear_boton_plantilla(self, ruta: str) -> QPushButton:
        """Crea el boton con logo de Corel para la columna Plantilla."""
        btn = QPushButton()
        btn.setToolTip(ruta if ruta else "Sin plantilla asignada")
        btn.setCursor(Qt.CursorShape.PointingHandCursor)

        if _COREL_ICON.exists():
            btn.setIcon(QIcon(str(_COREL_ICON)))
            
        if ruta:
            btn.setStyleSheet("""
                QPushButton {
                    border: none;
                    text-align: center;
                }
                QPushButton:hover { background-color: #96b7a2; }
            """)
            btn.clicked.connect(lambda: self._on_abrir_plantilla(ruta))
        else:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #cccccc;
                }
            """)
            btn.setEnabled(False)

        return btn

    def _refrescar_tabla(self):
        """Recarga todos los pedidos desde la BD y repinta la tabla."""
        pedidos = self._repo.get_all()
        self.tableWidget.setRowCount(0)
        for pedido in pedidos:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)

            # Celda 0: Cliente — guarda el id oculto para recuperarlo al seleccionar
            item_cliente = QTableWidgetItem(pedido.cliente)
            item_cliente.setData(Qt.ItemDataRole.UserRole, pedido.id)
            self.tableWidget.setItem(row, 0, item_cliente)

            self.tableWidget.setItem(row, 1, QTableWidgetItem(pedido.tipo_trabajo))
            combo = self._crear_combo_estado(pedido.id, pedido.estado)
            self.tableWidget.setCellWidget(row, 2, combo)
            self.tableWidget.setItem(row, 3, QTableWidgetItem(pedido.fecha_solicitud))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(pedido.fecha_entrega))

            # Columna 5: boton con logo de Corel que abre el archivo .cdr
            btn = self._crear_boton_plantilla(pedido.plantilla)
            self.tableWidget.setCellWidget(row, 5, btn)

            self.tableWidget.setItem(row, 6, QTableWidgetItem(""))
