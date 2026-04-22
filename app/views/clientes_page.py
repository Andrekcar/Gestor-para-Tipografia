# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clientes_page.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QPlainTextEdit, QSizePolicy, QTableWidget,
    QTableWidgetItem, QToolButton, QVBoxLayout, QWidget)

class clientesPage(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1499, 790)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_contenedor = QFrame(self.centralwidget)
        self.frame_contenedor.setObjectName(u"frame_contenedor")
        self.frame_contenedor.setStyleSheet(u"")
        self.frame_contenedor.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_contenedor.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_contenedor.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_contenedor)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QFrame(self.frame_contenedor)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMinimumSize(QSize(250, 0))
        self.sidebar.setMaximumSize(QSize(250, 16777215))
        self.sidebar.setStyleSheet(u"background-color: rgb(13, 37, 48);")
        self.sidebar.setFrameShape(QFrame.Shape.NoFrame)
        self.sidebar.setFrameShadow(QFrame.Shadow.Plain)
        self.sidebar.setLineWidth(0)
        self.labelNegocio = QLabel(self.sidebar)
        self.labelNegocio.setObjectName(u"labelNegocio")
        self.labelNegocio.setGeometry(QRect(80, 10, 151, 61))
        self.labelNegocio.setStyleSheet(u"\n"
"font: 700 15pt \"Segoe UI\";\n"
"")
        self.toolButtonPedidos = QToolButton(self.sidebar)
        self.toolButtonPedidos.setObjectName(u"toolButtonPedidos")
        self.toolButtonPedidos.setGeometry(QRect(20, 150, 211, 41))
        self.toolButtonPedidos.setStyleSheet(u"font: 13pt \"Segoe UI\";")
        self.toolButtonClientes = QToolButton(self.sidebar)
        self.toolButtonClientes.setObjectName(u"toolButtonClientes")
        self.toolButtonClientes.setGeometry(QRect(20, 100, 211, 41))
        self.toolButtonClientes.setStyleSheet(u"font: 13pt \"Segoe UI\";\n"
"border-color: rgb(255, 255, 255);")
        self.imgCliente = QLabel(self.sidebar)
        self.imgCliente.setObjectName(u"imgCliente")
        self.imgCliente.setGeometry(QRect(40, 100, 41, 41))
        self.imgCliente.setPixmap(QPixmap(u":/app/assets/nueva-cuenta.png"))
        self.imgCliente.setScaledContents(True)
        self.imgPedidos = QLabel(self.sidebar)
        self.imgPedidos.setObjectName(u"imgPedidos")
        self.imgPedidos.setGeometry(QRect(40, 150, 41, 41))
        self.imgPedidos.setPixmap(QPixmap(u":/app/assets/pedido.png"))
        self.imgPedidos.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.sidebar)

        self.frame_principal = QFrame(self.frame_contenedor)
        self.frame_principal.setObjectName(u"frame_principal")
        self.frame_principal.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_principal.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_principal.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame_principal)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.frame_principal)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 70))
        self.header.setMaximumSize(QSize(16777215, 70))
        self.header.setStyleSheet(u"background-color: rgb(240, 244, 245);\n"
"border-color: rgb(212, 230, 234);\n"
"\n"
"\n"
"")
        self.header.setFrameShape(QFrame.Shape.NoFrame)
        self.header.setFrameShadow(QFrame.Shadow.Plain)
        self.header.setLineWidth(0)
        self.labelTitulo = QLabel(self.header)
        self.labelTitulo.setObjectName(u"labelTitulo")
        self.labelTitulo.setGeometry(QRect(40, 10, 181, 61))
        self.labelTitulo.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 15pt \"Segoe UI\";\n"
"\n"
"")

        self.verticalLayout.addWidget(self.header)

        self.frame_contenido = QFrame(self.frame_principal)
        self.frame_contenido.setObjectName(u"frame_contenido")
        self.frame_contenido.setStyleSheet(u"border-top: 1px solid #e0e0e0;")
        self.frame_contenido.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_contenido.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_contenido.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_contenido)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_pedidos = QFrame(self.frame_contenido)
        self.frame_pedidos.setObjectName(u"frame_pedidos")
        self.frame_pedidos.setStyleSheet(u"background-color: rgb(240, 244, 245);")
        self.frame_pedidos.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pedidos.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_pedidos)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frameFiltro = QFrame(self.frame_pedidos)
        self.frameFiltro.setObjectName(u"frameFiltro")
        self.frameFiltro.setMinimumSize(QSize(0, 42))
        self.frameFiltro.setMaximumSize(QSize(16777215, 42))
        self.frameFiltro.setAutoFillBackground(False)
        self.frameFiltro.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"border: none;\n"
"border-radius: 5px;")
        self.frameFiltro.setFrameShape(QFrame.Shape.NoFrame)
        self.frameFiltro.setFrameShadow(QFrame.Shadow.Plain)
        self.frameFiltro.setLineWidth(0)
        self.comboBoxCliente = QComboBox(self.frameFiltro)
        self.comboBoxCliente.setObjectName(u"comboBoxCliente")
        self.comboBoxCliente.setGeometry(QRect(30, 0, 171, 41))
        self.comboBoxCliente.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(1, 1, 1, 50);")
        self.toolButtonBuscar = QToolButton(self.frameFiltro)
        self.toolButtonBuscar.setObjectName(u"toolButtonBuscar")
        self.toolButtonBuscar.setGeometry(QRect(770, 0, 91, 41))
        self.toolButtonBuscar.setStyleSheet(u"font: 13pt \"Segoe UI\";\n"
"background-color: rgb(29, 140, 160);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.frameFiltro)

        self.frameTabla = QFrame(self.frame_pedidos)
        self.frameTabla.setObjectName(u"frameTabla")
        self.frameTabla.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameTabla.sizePolicy().hasHeightForWidth())
        self.frameTabla.setSizePolicy(sizePolicy)
        self.frameTabla.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(1, 1, 1, 50);\n"
"border-radius: 10px;")
        self.frameTabla.setFrameShape(QFrame.Shape.NoFrame)
        self.frameTabla.setFrameShadow(QFrame.Shadow.Plain)
        self.frameTabla.setLineWidth(0)
        self.tableWidget = QTableWidget(self.frameTabla)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 80, 831, 481))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";\n"
"border-radius: 3px;")
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.toolButtonAdd = QToolButton(self.frameTabla)
        self.toolButtonAdd.setObjectName(u"toolButtonAdd")
        self.toolButtonAdd.setGeometry(QRect(700, 20, 161, 41))
        self.toolButtonAdd.setStyleSheet(u"font: 13pt \"Segoe UI\";\n"
"background-color: rgb(29, 140, 160);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.verticalLayout_2.addWidget(self.frameTabla)


        self.horizontalLayout_3.addWidget(self.frame_pedidos)

        self.frame_detalle = QFrame(self.frame_contenido)
        self.frame_detalle.setObjectName(u"frame_detalle")
        self.frame_detalle.setMinimumSize(QSize(350, 0))
        self.frame_detalle.setMaximumSize(QSize(350, 16777215))
        self.frame_detalle.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"")
        self.frame_detalle.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_detalle.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_detalle.setLineWidth(0)
        self.frame_detalle.setMidLineWidth(0)
        self.lineCliente = QLineEdit(self.frame_detalle)
        self.lineCliente.setObjectName(u"lineCliente")
        self.lineCliente.setGeometry(QRect(30, 90, 291, 41))
        self.lineCliente.setStyleSheet(u"border-color: rgb(0, 89, 255);\n"
"border: 1px solid rgba(1, 1, 1, 50);")
        self.lineTrabajo = QLineEdit(self.frame_detalle)
        self.lineTrabajo.setObjectName(u"lineTrabajo")
        self.lineTrabajo.setGeometry(QRect(30, 160, 291, 41))
        self.lineTrabajo.setStyleSheet(u"border-color: rgb(0, 89, 255);\n"
"border: 1px solid rgba(1, 1, 1, 50);")
        self.label_Nombre = QLabel(self.frame_detalle)
        self.label_Nombre.setObjectName(u"label_Nombre")
        self.label_Nombre.setGeometry(QRect(30, 80, 41, 16))
        self.label_Nombre.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.label_Telefono = QLabel(self.frame_detalle)
        self.label_Telefono.setObjectName(u"label_Telefono")
        self.label_Telefono.setGeometry(QRect(30, 150, 51, 16))
        self.label_Telefono.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.toolButtonGuardar = QToolButton(self.frame_detalle)
        self.toolButtonGuardar.setObjectName(u"toolButtonGuardar")
        self.toolButtonGuardar.setGeometry(QRect(30, 610, 141, 41))
        self.toolButtonGuardar.setStyleSheet(u"font: 13pt \"Segoe UI\";\n"
"background-color: rgb(29, 140, 160);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.toolButtonEliminar = QToolButton(self.frame_detalle)
        self.toolButtonEliminar.setObjectName(u"toolButtonEliminar")
        self.toolButtonEliminar.setGeometry(QRect(180, 610, 141, 41))
        self.toolButtonEliminar.setStyleSheet(u"font: 13pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 5px;")
        self.label_Cliente = QLabel(self.frame_detalle)
        self.label_Cliente.setObjectName(u"label_Cliente")
        self.label_Cliente.setGeometry(QRect(30, 20, 161, 41))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(13)
        font.setWeight(QFont.Weight.Bold)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_Cliente.setFont(font)
        self.label_Cliente.setStyleSheet(u"color: rgb(36, 36, 36);\n"
"font: 1000 13pt \"Segoe UI\";")
        self.lineEmail = QLineEdit(self.frame_detalle)
        self.lineEmail.setObjectName(u"lineEmail")
        self.lineEmail.setGeometry(QRect(30, 230, 291, 41))
        self.lineEmail.setStyleSheet(u"border-color: rgb(0, 89, 255);\n"
"border: 1px solid rgba(1, 1, 1, 50);")
        self.label_Email = QLabel(self.frame_detalle)
        self.label_Email.setObjectName(u"label_Email")
        self.label_Email.setGeometry(QRect(30, 220, 31, 16))
        self.label_Email.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.lineDireccion = QLineEdit(self.frame_detalle)
        self.lineDireccion.setObjectName(u"lineDireccion")
        self.lineDireccion.setGeometry(QRect(30, 300, 291, 41))
        self.lineDireccion.setStyleSheet(u"border-color: rgb(0, 89, 255);\n"
"border: 1px solid rgba(1, 1, 1, 50);")
        self.label_Direccion = QLabel(self.frame_detalle)
        self.label_Direccion.setObjectName(u"label_Direccion")
        self.label_Direccion.setGeometry(QRect(30, 290, 61, 16))
        self.label_Direccion.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.plainTextNotas = QPlainTextEdit(self.frame_detalle)
        self.plainTextNotas.setObjectName(u"plainTextNotas")
        self.plainTextNotas.setGeometry(QRect(30, 390, 291, 121))
        self.plainTextNotas.setStyleSheet(u"border-color: rgb(0, 89, 255);\n"
"border: 1px solid rgba(1, 1, 1, 50);")
        self.label_Notas = QLabel(self.frame_detalle)
        self.label_Notas.setObjectName(u"label_Notas")
        self.label_Notas.setGeometry(QRect(30, 380, 41, 16))
        self.label_Notas.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.lineCliente.raise_()
        self.lineTrabajo.raise_()
        self.label_Nombre.raise_()
        self.label_Telefono.raise_()
        self.toolButtonGuardar.raise_()
        self.label_Cliente.raise_()
        self.toolButtonEliminar.raise_()
        self.lineEmail.raise_()
        self.label_Email.raise_()
        self.lineDireccion.raise_()
        self.label_Direccion.raise_()
        self.plainTextNotas.raise_()
        self.label_Notas.raise_()

        self.horizontalLayout_3.addWidget(self.frame_detalle)


        self.verticalLayout.addWidget(self.frame_contenido)


        self.horizontalLayout_2.addWidget(self.frame_principal)


        self.horizontalLayout.addWidget(self.frame_contenedor)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelNegocio.setText(QCoreApplication.translate("MainWindow", u"Grafic\u00e1s Boyac\u00e1", None))
        self.toolButtonPedidos.setText(QCoreApplication.translate("MainWindow", u"Pedidos", None))
        self.toolButtonClientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.imgCliente.setText("")
        self.imgPedidos.setText("")
        self.labelTitulo.setText(QCoreApplication.translate("MainWindow", u"Gestor de Clientes", None))
        self.toolButtonBuscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None))
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Fecha Creaci\u00f3n", None))
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Notas", None))
        self.toolButtonAdd.setText(QCoreApplication.translate("MainWindow", u"+ Nuevo Cliente", None))
        self.label_Nombre.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_Telefono.setText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.toolButtonGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.toolButtonEliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.label_Cliente.setText(QCoreApplication.translate("MainWindow", u"Cliente ID-01", None))
        self.label_Email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_Direccion.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None))
        self.label_Notas.setText(QCoreApplication.translate("MainWindow", u"Notas", None))
    # retranslateUi


# ── Widget embebible con lógica CRUD ──────────────────────────────────────────

from app.models.cliente_repository import Cliente, ClienteRepository


class ClientesPage(QWidget):
    """
    QWidget que contiene únicamente el área de contenido del .ui
    (frame_clientes + frame_detalle), listo para embeber en horizontalLayout_3
    de MainWindow.  No incluye sidebar ni header propios del .ui.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self._repo = ClienteRepository()
        self._cliente_actual: Cliente | None = None

        self._build_ui()
        self._configurar_tabla()
        self._connect_signals()
        self._refrescar_tabla()

    # ── Construcción ──────────────────────────────────────────────────────────

    def _build_ui(self):
        root = QHBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)
        root.addWidget(self._build_frame_clientes())
        root.addWidget(self._build_frame_detalle())

    def _build_frame_clientes(self) -> QFrame:
        self.frame_clientes = QFrame()
        self.frame_clientes.setObjectName(u"frame_clientes")
        self.frame_clientes.setStyleSheet(u"background-color: rgb(240, 244, 245);")
        self.frame_clientes.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_clientes.setFrameShadow(QFrame.Shadow.Raised)

        vlay = QVBoxLayout(self.frame_clientes)
        vlay.setObjectName(u"verticalLayout_2")

        # ── frameFiltro con layout horizontal ─────────────────────────────────
        self.frameFiltro = QFrame()
        self.frameFiltro.setObjectName(u"frameFiltro")
        self.frameFiltro.setFixedHeight(42)
        self.frameFiltro.setStyleSheet(
            u"background-color: transparent; border: none; border-radius: 5px;"
        )
        self.frameFiltro.setFrameShape(QFrame.Shape.NoFrame)
        self.frameFiltro.setFrameShadow(QFrame.Shadow.Plain)
        self.frameFiltro.setLineWidth(0)

        filtro_hlay = QHBoxLayout(self.frameFiltro)
        filtro_hlay.setContentsMargins(0, 0, 0, 0)
        filtro_hlay.setSpacing(8)

        self.comboBoxCliente = QComboBox()
        self.comboBoxCliente.setObjectName(u"comboBoxCliente")
        self.comboBoxCliente.setMinimumWidth(171)
        self.comboBoxCliente.setMaximumWidth(280)
        self.comboBoxCliente.setFixedHeight(41)
        self.comboBoxCliente.setStyleSheet(
            u"color: rgb(0, 0, 0);\n"
            u"background-color: rgb(255, 255, 255);\n"
            u"border: 1px solid rgba(1, 1, 1, 50);"
        )

        self.toolButtonBuscar = QToolButton()
        self.toolButtonBuscar.setObjectName(u"toolButtonBuscar")
        self.toolButtonBuscar.setFixedSize(QSize(91, 41))
        self.toolButtonBuscar.setStyleSheet(
            u"font: 13pt \"Segoe UI\";\n"
            u"background-color: rgb(29, 140, 160);\n"
            u"color: rgb(255, 255, 255);"
        )
        self.toolButtonBuscar.setText(u"Buscar")

        filtro_hlay.addWidget(self.comboBoxCliente)
        filtro_hlay.addStretch()
        filtro_hlay.addWidget(self.toolButtonBuscar)

        vlay.addWidget(self.frameFiltro)

        # ── frameTabla con layout vertical ────────────────────────────────────
        self.frameTabla = QFrame()
        self.frameTabla.setObjectName(u"frameTabla")
        sp = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.frameTabla.setSizePolicy(sp)
        self.frameTabla.setStyleSheet(
            u"background-color: rgb(255, 255, 255);\n"
            u"border: 1px solid rgba(1, 1, 1, 50);\n"
            u"border-radius: 10px;"
        )
        self.frameTabla.setFrameShape(QFrame.Shape.NoFrame)
        self.frameTabla.setFrameShadow(QFrame.Shadow.Plain)
        self.frameTabla.setLineWidth(0)

        tabla_vlay = QVBoxLayout(self.frameTabla)
        tabla_vlay.setContentsMargins(9, 9, 9, 9)
        tabla_vlay.setSpacing(6)

        # Fila superior: stretch + botón Nuevo
        header_hlay = QHBoxLayout()
        header_hlay.addStretch()
        self.toolButtonAdd = QToolButton()
        self.toolButtonAdd.setObjectName(u"toolButtonAdd")
        self.toolButtonAdd.setFixedSize(QSize(161, 41))
        self.toolButtonAdd.setStyleSheet(
            u"font: 13pt \"Segoe UI\";\n"
            u"background-color: rgb(29, 140, 160);\n"
            u"color: rgb(255, 255, 255);\n"
            u"border-radius: 5px;"
        )
        self.toolButtonAdd.setText(u"+ Nuevo Cliente")
        header_hlay.addWidget(self.toolButtonAdd)
        tabla_vlay.addLayout(header_hlay)

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSizePolicy(
            QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        )
        self.tableWidget.setStyleSheet(
            u"color: rgb(0, 0, 0);\nfont: 700 9pt \"Segoe UI\";\nborder-radius: 3px;"
        )
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        tabla_vlay.addWidget(self.tableWidget)

        vlay.addWidget(self.frameTabla)
        return self.frame_clientes

    def _build_frame_detalle(self) -> QFrame:
        self.frame_detalle = QFrame()
        self.frame_detalle.setObjectName(u"frame_detalle")
        self.frame_detalle.setMinimumSize(QSize(350, 0))
        self.frame_detalle.setMaximumSize(QSize(350, 16777215))
        self.frame_detalle.setStyleSheet(
            u"background-color: rgb(255, 255, 255);\nborder: none;\n"
        )
        self.frame_detalle.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_detalle.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_detalle.setLineWidth(0)
        self.frame_detalle.setMidLineWidth(0)

        # Título
        font_titulo = QFont()
        font_titulo.setFamilies([u"Segoe UI"])
        font_titulo.setPointSize(13)
        font_titulo.setWeight(QFont.Weight.Bold)
        font_titulo.setKerning(False)

        self.label_Cliente = QLabel(u"Cliente ID-01", self.frame_detalle)
        self.label_Cliente.setObjectName(u"label_Cliente")
        self.label_Cliente.setGeometry(QRect(30, 20, 161, 41))
        self.label_Cliente.setFont(font_titulo)
        self.label_Cliente.setStyleSheet(
            u"color: rgb(36, 36, 36);\nfont: 1000 13pt \"Segoe UI\";"
        )

        _style_lbl = u"color: rgb(0, 0, 0);\nfont: 700 9pt \"Segoe UI\";"
        _style_inp = u"border-color: rgb(0, 89, 255);\nborder: 1px solid rgba(1, 1, 1, 50);"

        # Nombre
        self.label_Nombre = QLabel(u"Nombre", self.frame_detalle)
        self.label_Nombre.setObjectName(u"label_Nombre")
        self.label_Nombre.setGeometry(QRect(30, 80, 51, 16))
        self.label_Nombre.setStyleSheet(_style_lbl)
        
        self.lineNombre = QLineEdit(self.frame_detalle)
        self.lineNombre.setObjectName(u"lineCliente")
        self.lineNombre.setGeometry(QRect(30, 90, 291, 41))
        self.lineNombre.setStyleSheet(_style_inp)
        self.label_Nombre.raise_()
        

        # Telefono
        self.label_Telefono = QLabel(u"Telefono", self.frame_detalle)
        self.label_Telefono.setObjectName(u"label_Telefono")
        self.label_Telefono.setGeometry(QRect(30, 150, 51, 16))
        self.label_Telefono.setStyleSheet(_style_lbl)

        self.lineTelefono = QLineEdit(self.frame_detalle)
        self.lineTelefono.setObjectName(u"lineTrabajo")
        self.lineTelefono.setGeometry(QRect(30, 160, 291, 41))
        self.lineTelefono.setStyleSheet(_style_inp)
        self.label_Telefono.raise_()

        # Email
        self.label_Email = QLabel(u"Email", self.frame_detalle)
        self.label_Email.setObjectName(u"label_Email")
        self.label_Email.setGeometry(QRect(30, 220, 31, 16))
        self.label_Email.setStyleSheet(_style_lbl)

        self.lineEmail = QLineEdit(self.frame_detalle)
        self.lineEmail.setObjectName(u"lineEmail")
        self.lineEmail.setGeometry(QRect(30, 230, 291, 41))
        self.lineEmail.setStyleSheet(_style_inp)
        self.label_Email.raise_()

        # Dirección
        self.label_Direccion = QLabel(u"Dirección", self.frame_detalle)
        self.label_Direccion.setObjectName(u"label_Direccion")
        self.label_Direccion.setGeometry(QRect(30, 290, 61, 16))
        self.label_Direccion.setStyleSheet(_style_lbl)

        self.lineDireccion = QLineEdit(self.frame_detalle)
        self.lineDireccion.setObjectName(u"lineDireccion")
        self.lineDireccion.setGeometry(QRect(30, 300, 291, 41))
        self.lineDireccion.setStyleSheet(_style_inp)
        self.label_Direccion.raise_()

        # Notas
        self.label_Notas = QLabel(u"Notas", self.frame_detalle)
        self.label_Notas.setObjectName(u"label_Notas")
        self.label_Notas.setGeometry(QRect(30, 380, 41, 16))
        self.label_Notas.setStyleSheet(_style_lbl)

        self.plainTextNotas = QPlainTextEdit(self.frame_detalle)
        self.plainTextNotas.setObjectName(u"plainTextNotas")
        self.plainTextNotas.setGeometry(QRect(30, 390, 291, 121))
        self.plainTextNotas.setStyleSheet(_style_inp)
        self.label_Notas.raise_()
        
        # Botones
        self.toolButtonGuardar = QToolButton(self.frame_detalle)
        self.toolButtonGuardar.setObjectName(u"toolButtonGuardar")
        self.toolButtonGuardar.setGeometry(QRect(30, 610, 141, 41))
        self.toolButtonGuardar.setStyleSheet(
            u"font: 13pt \"Segoe UI\";\n"
            u"background-color: rgb(29, 140, 160);\n"
            u"color: rgb(255, 255, 255);\n"
            u"border-radius: 5px;"
        )
        self.toolButtonGuardar.setText(u"Guardar")

        self.toolButtonEliminar = QToolButton(self.frame_detalle)
        self.toolButtonEliminar.setObjectName(u"toolButtonEliminar")
        self.toolButtonEliminar.setGeometry(QRect(180, 610, 141, 41))
        self.toolButtonEliminar.setStyleSheet(
            u"font: 13pt \"Segoe UI\";\n"
            u"color: rgb(0, 0, 0);\n"
            u"background-color: rgb(255, 255, 255);\n"
            u"border-color: rgb(0, 0, 0);\n"
            u"border-radius: 5px;"
        )
        self.toolButtonEliminar.setText(u"Eliminar")

        return self.frame_detalle

    # ── Configuración ──────────────────────────────────────────────────────────

    def _configurar_tabla(self):
        for col, texto in enumerate(
            ["Nombre", "Telefono", "Email", "Dirección", "Fecha Creación", "Notas"]
        ):
            self.tableWidget.setHorizontalHeaderItem(col, QTableWidgetItem(texto))

        h = self.tableWidget.horizontalHeader()
        h.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableWidget.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )
        self.tableWidget.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)

    # ── Señales ────────────────────────────────────────────────────────────────

    def _connect_signals(self):
        self.toolButtonAdd.clicked.connect(self._on_nuevo)
        self.toolButtonGuardar.clicked.connect(self._on_guardar)
        self.toolButtonEliminar.clicked.connect(self._on_eliminar)
        self.toolButtonBuscar.clicked.connect(self._on_buscar)
        self.tableWidget.itemSelectionChanged.connect(self._on_seleccion_cambiada)

    # ── Slots ──────────────────────────────────────────────────────────────────

    def _on_nuevo(self):
        self._cliente_actual = None
        self.lineCliente.clear()
        self.lineTrabajo.clear()
        self.lineEmail.clear()
        self.lineDireccion.clear()
        self.plainTextNotas.clear()
        self.label_Cliente.setText(u"Nuevo Cliente")
        self.tableWidget.clearSelection()
        self.lineCliente.setFocus()

    def _on_guardar(self):
        nombre = self.lineCliente.text().strip()
        if not nombre:
            return

        datos = dict(
            nombre=nombre,
            telefono=self.lineTrabajo.text().strip(),
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

        self._refrescar_tabla()

    def _on_eliminar(self):
        if self._cliente_actual is None:
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
        self.lineCliente.setText(self._cliente_actual.nombre)
        self.lineTrabajo.setText(self._cliente_actual.telefono)
        self.lineEmail.setText(self._cliente_actual.email)
        self.lineDireccion.setText(self._cliente_actual.direccion)
        self.plainTextNotas.setPlainText(self._cliente_actual.notas)

    # ── Helpers ────────────────────────────────────────────────────────────────

    def _refrescar_tabla(self):
        clientes = self._repo.get_all()

        nombre_actual = self.comboBoxCliente.currentText()
        self.comboBoxCliente.blockSignals(True)
        self.comboBoxCliente.clear()
        self.comboBoxCliente.addItem(u"")
        for c in clientes:
            self.comboBoxCliente.addItem(c.nombre)
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
            self.tableWidget.setItem(row, 4, QTableWidgetItem(u""))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(cliente.notas))

