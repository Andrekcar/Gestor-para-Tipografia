from PySide6.QtCore import Qt, QStringListModel
from PySide6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QCompleter, QMessageBox
from app.models.cliente_repository import Cliente, ClienteRepository
from app.services.file_manager import crear_carpeta_cliente
from app.views.ui.ui_clientes_page import Ui_ClientesPage

class ClientesPage(QWidget, Ui_ClientesPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._repo = ClienteRepository()
        self._cliente_actual: Cliente | None = None

        self.setupUi(self)
        self._configurar_busqueda()
        self._configurar_tabla()
        self._connect_signals()
        self._refrescar_tabla()

    # ------------------------------------------------------------------
    # Configuracion inicial
    # ------------------------------------------------------------------

    def _configurar_busqueda(self):
        self._modelo_busqueda = QStringListModel()
        completer = QCompleter(self._modelo_busqueda, self)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self.comboBoxCliente.setCompleter(completer)

    def _configurar_tabla(self):
        for col, texto in enumerate(["Nombre", "Telefono", "Email", "Dirección"]):
            self.tableWidget.setHorizontalHeaderItem(col, QTableWidgetItem(texto))
        h = self.tableWidget.horizontalHeader()
        h.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tableWidget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)

    # ------------------------------------------------------------------
    # Conexion de señales
    # ------------------------------------------------------------------

    def _connect_signals(self):
        self.toolButtonAdd.clicked.connect(self._on_nuevo)
        self.toolButtonGuardar.clicked.connect(self._on_guardar)
        self.toolButtonEliminar.clicked.connect(self._on_eliminar)
        self.toolButtonBuscar.clicked.connect(self._on_buscar)
        self.tableWidget.itemSelectionChanged.connect(self._on_seleccion_cambiada)

    # ------------------------------------------------------------------
    # Slots
    # ------------------------------------------------------------------

    def _on_nuevo(self):
        self._cliente_actual = None
        self.lineNombre.clear()
        self.lineTelefono.clear()
        self.lineEmail.clear()
        self.lineDireccion.clear()
        self.plainTextNotas.clear()
        self.label_Cliente.setText(u"Nuevo Cliente")
        self.tableWidget.clearSelection()
        self.lineNombre.setFocus()

    def _on_guardar(self):
        nombre = self.lineNombre.text().strip()
        if not nombre:
            return

        exclude_id = self._cliente_actual.id if self._cliente_actual else None
        if self._repo.exists_by_nombre(nombre, exclude_id):
            QMessageBox.warning(self, "Cliente duplicado", f'Ya existe un cliente con el nombre "{nombre}".')
            return

        datos = dict(
            nombre=nombre,
            telefono=self.lineTelefono.text().strip(),
            email=self.lineEmail.text().strip(),
            direccion=self.lineDireccion.text().strip(),
            notas=self.plainTextNotas.toPlainText().strip(),
        )

        if self._cliente_actual is not None:
            for k, v in datos.items():
                setattr(self._cliente_actual, k, v)
            self._repo.update(self._cliente_actual)
        else:
            self._cliente_actual = self._repo.insert(Cliente(**datos))
            crear_carpeta_cliente(self._cliente_actual.nombre)

        self._refrescar_tabla()

    def _on_eliminar(self):
        if self._cliente_actual is None:
            return
        respuesta = QMessageBox.question(
            self, "Eliminar cliente",
            f"¿Eliminar a {self._cliente_actual.nombre}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if respuesta != QMessageBox.StandardButton.Yes:
            return
        self._repo.delete(self._cliente_actual.id)
        self._cliente_actual = None
        self._on_nuevo()
        self._refrescar_tabla()

    def _on_buscar(self):
        texto = self.comboBoxCliente.currentText().strip().lower()
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 0)
            coincide = texto in (item.text().lower() if item else "")
            self.tableWidget.setRowHidden(row, not coincide and bool(texto))

    def _on_seleccion_cambiada(self):
        row = self.tableWidget.currentRow()
        if row < 0:
            return
        celda = self.tableWidget.item(row, 0)
        if celda is None:
            return
        cliente_id = celda.data(Qt.ItemDataRole.UserRole)
        self._cliente_actual = self._repo.get_by_id(cliente_id)
        if self._cliente_actual is None:
            return

        self.label_Cliente.setText(f"Cliente ID-{self._cliente_actual.id}")
        self.lineNombre.setText(self._cliente_actual.nombre)
        self.lineTelefono.setText(self._cliente_actual.telefono)
        self.lineEmail.setText(self._cliente_actual.email)
        self.lineDireccion.setText(self._cliente_actual.direccion)
        self.plainTextNotas.setPlainText(self._cliente_actual.notas)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _refrescar_tabla(self):
        clientes = self._repo.get_all()
        nombres = [c.nombre for c in clientes]
        self._modelo_busqueda.setStringList(nombres)

        nombre_actual = self.comboBoxCliente.currentText()
        self.comboBoxCliente.blockSignals(True)
        self.comboBoxCliente.clear()
        self.comboBoxCliente.addItem(u"")
        self.comboBoxCliente.addItems(nombres)
        idx = self.comboBoxCliente.findText(nombre_actual)
        self.comboBoxCliente.setCurrentIndex(max(idx, 0))
        self.comboBoxCliente.blockSignals(False)

        self.tableWidget.setRowCount(0)
        for cliente in clientes:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            item_nombre = QTableWidgetItem(cliente.nombre)
            item_nombre.setData(Qt.ItemDataRole.UserRole, cliente.id)
            self.tableWidget.setItem(row, 0, item_nombre)
            self.tableWidget.setItem(row, 1, QTableWidgetItem(cliente.telefono))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(cliente.email))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(cliente.direccion))
