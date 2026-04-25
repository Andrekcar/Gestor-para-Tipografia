# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from pathlib import Path
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpinBox, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
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
        self.label_logogb = QLabel(self.sidebar)
        self.label_logogb.setObjectName(u"label_logogb")
        self.label_logogb.setGeometry(QRect(10, 10, 60, 60))
        self.label_logogb.setMinimumSize(QSize(60, 60))
        self.label_logogb.setScaledContents(True)
        self.labelNegocio = QLabel(self.sidebar)
        self.labelNegocio.setObjectName(u"labelNegocio")
        self.labelNegocio.setGeometry(QRect(80, 10, 151, 61))
        self.labelNegocio.setStyleSheet(u"font: 700 15pt \"Segoe UI\"; color: rgb(255, 255, 255);")
        self.toolButtonPedidos = QToolButton(self.sidebar)
        self.toolButtonPedidos.setObjectName(u"toolButtonPedidos")
        self.toolButtonPedidos.setGeometry(QRect(20, 150, 211, 41))
        self.toolButtonPedidos.setStyleSheet(u"font: 13pt \"Segoe UI\"; color: rgb(255, 255, 255); border: 2px solid rgb(255, 255, 255); border-radius: 6px;")
        self.toolButtonClientes = QToolButton(self.sidebar)
        self.toolButtonClientes.setObjectName(u"toolButtonClientes")
        self.toolButtonClientes.setGeometry(QRect(20, 100, 211, 41))
        self.toolButtonClientes.setStyleSheet(u"font: 13pt \"Segoe UI\"; color: rgb(255, 255, 255); border: 2px solid rgb(255, 255, 255); border-radius: 6px;")
        self.label = QLabel(self.sidebar)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 100, 41, 41))
        self.label.setPixmap(QPixmap(str(Path(__file__).resolve().parents[2] / "assets" / "nueva-cuenta.png")))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.sidebar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 150, 41, 41))
        self.label_2.setPixmap(QPixmap(str(Path(__file__).resolve().parents[2] / "assets" / "pedido.png")))
        self.label_2.setScaledContents(True)

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
        self.frameFiltro.setFixedHeight(42)
        self.frameFiltro.setAutoFillBackground(False)
        self.frameFiltro.setStyleSheet(u"background-color: transparent;\nborder: none;\nborder-radius: 5px;")
        self.frameFiltro.setFrameShape(QFrame.Shape.NoFrame)
        self.frameFiltro.setFrameShadow(QFrame.Shadow.Plain)
        self.frameFiltro.setLineWidth(0)

        filtro_hlay = QHBoxLayout(self.frameFiltro)
        filtro_hlay.setContentsMargins(0, 0, 0, 0)
        filtro_hlay.setSpacing(8)

        # Filtro por cliente 
        self.comboBoxCliente = QComboBox()
        self.comboBoxCliente.setObjectName(u"comboBoxCliente")
        self.comboBoxCliente.setFixedSize(QSize(171, 41))
        self.comboBoxCliente.setEditable(True)
        self.comboBoxCliente.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.comboBoxCliente.setPlaceholderText("Cliente...")
        self.comboBoxCliente.setStyleSheet(u"color: rgb(0, 0, 0);\nbackground-color: rgb(255, 255, 255);\nborder: 1px solid rgba(1, 1, 1, 50);")

        # Filtro por tipo de trabajo
        self.lineEditTrabajo = QLineEdit()
        self.lineEditTrabajo.setObjectName(u"lineEditTrabajo")
        self.lineEditTrabajo.setFixedSize(QSize(141, 41))
        self.lineEditTrabajo.setPlaceholderText("Tipo de trabajo...")
        self.lineEditTrabajo.setStyleSheet(u"color: rgb(0, 0, 0);\nbackground-color: rgb(255, 255, 255);\nborder: 1px solid rgba(1, 1, 1, 50);")

        # Filtro por estado
        self.comboBoxEstado = QComboBox()
        self.comboBoxEstado.addItem("Todos")
        self.comboBoxEstado.addItem("No Iniciado")
        self.comboBoxEstado.addItem("En Progreso")
        self.comboBoxEstado.addItem("Entregado")
        self.comboBoxEstado.setObjectName(u"comboBoxEstado")
        self.comboBoxEstado.setFixedSize(QSize(121, 41))
        self.comboBoxEstado.setStyleSheet(u"color: rgb(0, 0, 0);\nbackground-color: rgb(255, 255, 255);\nborder: 1px solid rgba(1, 1, 1, 50);")

        # Placeholder para el selector de rango de fechas
        self.frame_fecha_rango = QFrame()
        self.frame_fecha_rango.setObjectName(u"frame_fecha_rango")
        self.frame_fecha_rango.setFixedSize(QSize(260, 41))
        self.frame_fecha_rango.setFrameShape(QFrame.Shape.NoFrame)

        self.toolButtonBuscar = QToolButton()
        self.toolButtonBuscar.setObjectName(u"toolButtonBuscar")
        self.toolButtonBuscar.setFixedSize(QSize(91, 41))
        self.toolButtonBuscar.setStyleSheet(u"font: 13pt \"Segoe UI\";\nbackground-color: rgb(29, 140, 160);\ncolor: rgb(255, 255, 255);")

        filtro_hlay.addWidget(self.comboBoxCliente)
        filtro_hlay.addWidget(self.lineEditTrabajo)
        filtro_hlay.addWidget(self.comboBoxEstado)
        filtro_hlay.addWidget(self.frame_fecha_rango)
        filtro_hlay.addStretch()
        filtro_hlay.addWidget(self.toolButtonBuscar)

        self.verticalLayout_2.addWidget(self.frameFiltro)

        self.frameTabla = QFrame(self.frame_pedidos)
        self.frameTabla.setObjectName(u"frameTabla")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.frameTabla.setSizePolicy(sizePolicy)
        self.frameTabla.setStyleSheet(u"background-color: rgb(255, 255, 255);\nborder: 1px solid rgba(1, 1, 1, 50);\nborder-radius: 10px;")
        self.frameTabla.setFrameShape(QFrame.Shape.NoFrame)
        self.frameTabla.setFrameShadow(QFrame.Shadow.Plain)
        self.frameTabla.setLineWidth(0)

        tabla_vlay = QVBoxLayout(self.frameTabla)
        tabla_vlay.setContentsMargins(9, 9, 9, 9)
        tabla_vlay.setSpacing(6)

        header_hlay = QHBoxLayout()
        header_hlay.addStretch()
        self.toolButtonAdd = QToolButton()
        self.toolButtonAdd.setObjectName(u"toolButtonAdd")
        self.toolButtonAdd.setFixedSize(QSize(161, 41))
        self.toolButtonAdd.setStyleSheet(u"font: 13pt \"Segoe UI\";\nbackground-color: rgb(29, 140, 160);\ncolor: rgb(255, 255, 255);\nborder-radius: 5px;")
        header_hlay.addWidget(self.toolButtonAdd)
        tabla_vlay.addLayout(header_hlay)

        self.tableWidget = QTableWidget()
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
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
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setStyleSheet(u"color: rgb(0, 0, 0);\nfont: 700 9pt \"Segoe UI\";\nborder-radius: 3px;")
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        tabla_vlay.addWidget(self.tableWidget)

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
        self.label_Cliente = QLabel(self.frame_detalle)
        self.label_Cliente.setObjectName(u"label_Cliente")
        self.label_Cliente.setGeometry(QRect(30, 80, 41, 16))
        self.label_Cliente.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.label_Trabajo = QLabel(self.frame_detalle)
        self.label_Trabajo.setObjectName(u"label_Trabajo")
        self.label_Trabajo.setGeometry(QRect(30, 150, 91, 16))
        self.label_Trabajo.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.plainTextDescripcion = QPlainTextEdit(self.frame_detalle)
        self.plainTextDescripcion.setObjectName(u"plainTextDescripcion")
        self.plainTextDescripcion.setGeometry(QRect(30, 230, 291, 111))
        self.plainTextDescripcion.setStyleSheet(u"border-color: rgb(0, 89, 255);\n"
"border: 1px solid rgba(1, 1, 1, 50);")
        self.label_Descripcion = QLabel(self.frame_detalle)
        self.label_Descripcion.setObjectName(u"label_Descripcion")
        self.label_Descripcion.setGeometry(QRect(30, 220, 71, 16))
        self.label_Descripcion.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.label_Und = QLabel(self.frame_detalle)
        self.label_Und.setObjectName(u"label_Und")
        self.label_Und.setGeometry(QRect(30, 360, 71, 16))
        self.label_Und.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.spinBoxUnd = QSpinBox(self.frame_detalle)
        self.spinBoxUnd.setObjectName(u"spinBoxUnd")
        self.spinBoxUnd.setGeometry(QRect(30, 370, 291, 40))
        self.spinBoxUnd.setMinimum(1)
        self.spinBoxUnd.setMaximum(99999)
        self.spinBoxUnd.setValue(1)
        self.spinBoxUnd.setStyleSheet(
            u"QSpinBox { color: rgb(0, 0, 0); border: 1px solid rgba(1, 1, 1, 50); font: 9pt \"Segoe UI\"; }\n"
            u"QSpinBox::up-button { width: 0; }\n"
            u"QSpinBox::down-button { width: 0; }"
        )
        self.label_Estado = QLabel(self.frame_detalle)
        self.label_Estado.setObjectName(u"label_Estado")
        self.label_Estado.setGeometry(QRect(30, 423, 41, 16))
        self.label_Estado.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.lineNo_iniciado = QLineEdit(self.frame_detalle)
        self.lineNo_iniciado.setObjectName(u"lineNo_iniciado")
        self.lineNo_iniciado.setGeometry(QRect(30, 443, 91, 31))
        self.lineNo_iniciado.setStyleSheet(u"\n"
"color: rgba(0, 0, 0, 0.7);\n"
"\n"
"font: 700 9pt \"Segoe UI\";\n"
"border-radius: 15px;\n"
"background-color: rgb(221, 240, 244);")
        self.linePlantilla = QLineEdit(self.frame_detalle)
        self.linePlantilla.setObjectName(u"linePlantilla")
        self.linePlantilla.setGeometry(QRect(30, 500, 291, 41))
        self.linePlantilla.setStyleSheet(u"border-color: rgb(0, 89, 255);\n"
"border: 1px solid rgba(1, 1, 1, 50);")
        self.lineEn_progreso = QLineEdit(self.frame_detalle)
        self.lineEn_progreso.setObjectName(u"lineEn_progreso")
        self.lineEn_progreso.setGeometry(QRect(130, 443, 91, 31))
        self.lineEn_progreso.setStyleSheet(u"\n"
"color: rgba(0, 0, 0, 0.7);\n"
"\n"
"font: 700 9pt \"Segoe UI\";\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 243, 204);")
        self.lineEntregado = QLineEdit(self.frame_detalle)
        self.lineEntregado.setObjectName(u"lineEntregado")
        self.lineEntregado.setGeometry(QRect(230, 443, 91, 31))
        self.lineEntregado.setStyleSheet(u"\n"
"color: rgba(0, 0, 0, 0.7);\n"
"font: 700 9pt \"Segoe UI\";\n"
"border-radius: 15px;\n"
"background-color: rgb(212, 245, 226);")
        self.label_Plantilla = QLabel(self.frame_detalle)
        self.label_Plantilla.setObjectName(u"label_Plantilla")
        self.label_Plantilla.setGeometry(QRect(30, 490, 51, 16))
        self.label_Plantilla.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.toolButtonGuardar = QToolButton(self.frame_detalle)
        self.toolButtonGuardar.setObjectName(u"toolButtonGuardar")
        self.toolButtonGuardar.setGeometry(QRect(30, 590, 128, 41))
        self.toolButtonGuardar.setStyleSheet(u"font: 13pt \"Segoe UI\";\n"
"background-color: rgb(29, 140, 160);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.toolButtonEliminar = QToolButton(self.frame_detalle)
        self.toolButtonEliminar.setObjectName(u"toolButtonEliminar")
        self.toolButtonEliminar.setGeometry(QRect(192, 590, 128, 41))
        self.toolButtonEliminar.setStyleSheet(u"font: 13pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 5px;")
        self.label_Orden = QLabel(self.frame_detalle)
        self.label_Orden.setObjectName(u"label_Orden")
        self.label_Orden.setGeometry(QRect(30, 20, 200, 41))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(13)
        font.setWeight(QFont.Weight.Bold)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_Orden.setFont(font)
        self.label_Orden.setStyleSheet(u"color: rgb(36, 36, 36);\n"
"font: 1000 13pt \"Segoe UI\";")
        self.pushButton_2 = QPushButton(self.frame_detalle)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(280, 510, 31, 21))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineCliente.raise_()
        self.lineTrabajo.raise_()
        self.label_Cliente.raise_()
        self.label_Trabajo.raise_()
        self.plainTextDescripcion.raise_()
        self.label_Descripcion.raise_()
        self.spinBoxUnd.raise_()
        self.label_Und.raise_()
        self.label_Estado.raise_()
        self.lineNo_iniciado.raise_()
        self.linePlantilla.raise_()
        self.lineEn_progreso.raise_()
        self.lineEntregado.raise_()
        self.label_Plantilla.raise_()
        self.toolButtonGuardar.raise_()
        self.label_Orden.raise_()
        self.toolButtonEliminar.raise_()
        self.pushButton_2.raise_()

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
        self.label.setText("")
        self.label_2.setText("")
        self.labelTitulo.setText(QCoreApplication.translate("MainWindow", u"Gestor de Pedidos", None))
        self.comboBoxEstado.setItemText(0, QCoreApplication.translate("MainWindow", u"Todos", None))
        self.comboBoxEstado.setItemText(1, QCoreApplication.translate("MainWindow", u"No Iniciado", None))
        self.comboBoxEstado.setItemText(2, QCoreApplication.translate("MainWindow", u"En Progreso", None))
        self.comboBoxEstado.setItemText(3, QCoreApplication.translate("MainWindow", u"Entregado", None))
        self.toolButtonBuscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tipo de Trabajo", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Und", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Fecha Solicitud", None))
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Fecha Entrega", None))
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Plantilla", None))
        self.toolButtonAdd.setText(QCoreApplication.translate("MainWindow", u"+ Nuevo Pedido", None))
        self.label_Cliente.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.label_Trabajo.setText(QCoreApplication.translate("MainWindow", u"Tipo de Trabajo", None))
        self.label_Descripcion.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None))
        self.label_Und.setText(QCoreApplication.translate("MainWindow", u"Unidades", None))
        self.label_Estado.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.lineNo_iniciado.setText(QCoreApplication.translate("MainWindow", u"    No iniciado", None))
        self.lineEn_progreso.setText(QCoreApplication.translate("MainWindow", u"   En Progreso", None))
        self.lineEntregado.setText(QCoreApplication.translate("MainWindow", u"     Entregado", None))
        self.label_Plantilla.setText(QCoreApplication.translate("MainWindow", u"Plantilla", None))
        self.toolButtonGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.toolButtonEliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.label_Orden.setText(QCoreApplication.translate("MainWindow", u"Orden ID-01", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"X", None))
    # retranslateUi

