# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PySide6.QtCore import QRect, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QComboBox, QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QSizePolicy, QTableWidget, QToolButton, QVBoxLayout,
)

class Ui_ClientesPage:
    def setupUi(self, widget):
        root = QHBoxLayout(widget)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)
        root.addWidget(self._build_frame_clientes())
        root.addWidget(self._build_frame_detalle())

    def _build_frame_clientes(self):
        self.frame_clientes = QFrame()
        self.frame_clientes.setObjectName(u"frame_clientes")
        self.frame_clientes.setStyleSheet(u"background-color: rgb(240, 244, 245);")
        self.frame_clientes.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_clientes.setFrameShadow(QFrame.Shadow.Raised)

        vlay = QVBoxLayout(self.frame_clientes)
        vlay.setObjectName(u"verticalLayout_clientes")

        # ── frameFiltro ───────────────────────────────────────────────────────
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
        self.comboBoxCliente.setEditable(True)
        self.comboBoxCliente.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.comboBoxCliente.setPlaceholderText(u"Buscar cliente...")
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

        # ── frameTabla ────────────────────────────────────────────────────────
        self.frameTabla = QFrame()
        self.frameTabla.setObjectName(u"frameTabla")
        self.frameTabla.setSizePolicy(
            QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        )
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
        self.tableWidget.setColumnCount(4)
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

    def _build_frame_detalle(self):
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

        font_titulo = QFont()
        font_titulo.setFamilies([u"Segoe UI"])
        font_titulo.setPointSize(13)
        font_titulo.setWeight(QFont.Weight.Bold)
        font_titulo.setKerning(False)

        _style_lbl = u"color: rgb(0, 0, 0);\nfont: 700 9pt \"Segoe UI\";"
        _style_inp = (
            u"color: rgb(0, 0, 0);\n"
            u"border-color: rgb(0, 89, 255);\n"
            u"border: 1px solid rgba(1, 1, 1, 50);"
        )

        self.label_Cliente = QLabel(u"Cliente ID-01", self.frame_detalle)
        self.label_Cliente.setObjectName(u"label_Cliente")
        self.label_Cliente.setGeometry(QRect(30, 20, 161, 41))
        self.label_Cliente.setFont(font_titulo)
        self.label_Cliente.setStyleSheet(
            u"color: rgb(36, 36, 36);\nfont: 1000 13pt \"Segoe UI\";"
        )

        self.label_Nombre = QLabel(u"Nombre", self.frame_detalle)
        self.label_Nombre.setObjectName(u"label_Nombre")
        self.label_Nombre.setGeometry(QRect(30, 80, 51, 16))
        self.label_Nombre.setStyleSheet(_style_lbl)
        self.lineNombre = QLineEdit(self.frame_detalle)
        self.lineNombre.setObjectName(u"lineNombre")
        self.lineNombre.setGeometry(QRect(30, 90, 291, 41))
        self.lineNombre.setStyleSheet(_style_inp)
        self.label_Nombre.raise_()

        self.label_Telefono = QLabel(u"Telefono", self.frame_detalle)
        self.label_Telefono.setObjectName(u"label_Telefono")
        self.label_Telefono.setGeometry(QRect(30, 150, 51, 16))
        self.label_Telefono.setStyleSheet(_style_lbl)
        self.lineTelefono = QLineEdit(self.frame_detalle)
        self.lineTelefono.setObjectName(u"lineTelefono")
        self.lineTelefono.setGeometry(QRect(30, 160, 291, 41))
        self.lineTelefono.setStyleSheet(_style_inp)
        self.label_Telefono.raise_()

        self.label_Email = QLabel(u"Email", self.frame_detalle)
        self.label_Email.setObjectName(u"label_Email")
        self.label_Email.setGeometry(QRect(30, 220, 31, 16))
        self.label_Email.setStyleSheet(_style_lbl)
        self.lineEmail = QLineEdit(self.frame_detalle)
        self.lineEmail.setObjectName(u"lineEmail")
        self.lineEmail.setGeometry(QRect(30, 230, 291, 41))
        self.lineEmail.setStyleSheet(_style_inp)
        self.label_Email.raise_()

        self.label_Direccion = QLabel(u"Dirección", self.frame_detalle)
        self.label_Direccion.setObjectName(u"label_Direccion")
        self.label_Direccion.setGeometry(QRect(30, 290, 61, 16))
        self.label_Direccion.setStyleSheet(_style_lbl)
        self.lineDireccion = QLineEdit(self.frame_detalle)
        self.lineDireccion.setObjectName(u"lineDireccion")
        self.lineDireccion.setGeometry(QRect(30, 300, 291, 41))
        self.lineDireccion.setStyleSheet(_style_inp)
        self.label_Direccion.raise_()

        self.label_Notas = QLabel(u"Notas", self.frame_detalle)
        self.label_Notas.setObjectName(u"label_Notas")
        self.label_Notas.setGeometry(QRect(30, 360, 41, 16))
        self.label_Notas.setStyleSheet(_style_lbl)
        self.plainTextNotas = QPlainTextEdit(self.frame_detalle)
        self.plainTextNotas.setObjectName(u"plainTextNotas")
        self.plainTextNotas.setGeometry(QRect(30, 370, 291, 121))
        self.plainTextNotas.setStyleSheet(_style_inp)
        self.label_Notas.raise_()

        self.toolButtonGuardar = QToolButton(self.frame_detalle)
        self.toolButtonGuardar.setObjectName(u"toolButtonGuardar")
        self.toolButtonGuardar.setGeometry(QRect(30, 590, 128, 41))
        self.toolButtonGuardar.setStyleSheet(
            u"font: 13pt \"Segoe UI\";\n"
            u"background-color: rgb(29, 140, 160);\n"
            u"color: rgb(255, 255, 255);\n"
            u"border-radius: 5px;"
        )
        self.toolButtonGuardar.setText(u"Guardar")

        self.toolButtonEliminar = QToolButton(self.frame_detalle)
        self.toolButtonEliminar.setObjectName(u"toolButtonEliminar")
        self.toolButtonEliminar.setGeometry(QRect(192, 590, 128, 41))
        self.toolButtonEliminar.setStyleSheet(
            u"font: 13pt \"Segoe UI\";\n"
            u"color: rgb(0, 0, 0);\n"
            u"background-color: rgb(255, 255, 255);\n"
            u"border-color: rgb(0, 0, 0);\n"
            u"border-radius: 5px;"
        )
        self.toolButtonEliminar.setText(u"Eliminar")

        return self.frame_detalle
