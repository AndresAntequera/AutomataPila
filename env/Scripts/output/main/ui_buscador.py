# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'buscador.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 690)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.centralwidget)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setEnabled(True)
        self.frame_superior.setMinimumSize(QSize(0, 40))
        self.frame_superior.setMaximumSize(QSize(16777215, 40))
        self.frame_superior.setStyleSheet(u"background-color: rgb(133, 146, 158);\n"
"")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Buscador = QPushButton(self.frame_superior)
        self.Buscador.setObjectName(u"Buscador")
        self.Buscador.setMinimumSize(QSize(0, 40))
        self.Buscador.setMaximumSize(QSize(16777215, 40))
        self.Buscador.setStyleSheet(u"border:0px;\n"
"margin: 5px 10px")
        icon = QIcon()
        icon.addFile(u"../assets/LUPA.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Buscador.setIcon(icon)
        self.Buscador.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.Buscador)

        self.horizontalSpacer = QSpacerItem(441, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.centralwidget)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lateral = QFrame(self.frame_inferior)
        self.lateral.setObjectName(u"lateral")
        self.lateral.setMinimumSize(QSize(200, 25))
        self.lateral.setMaximumSize(QSize(0, 16777215))
        self.lateral.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(33, 97, 140);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:rgb(0, 170, 255);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"\n"
"font: 75 12pt \"Arial Narrow\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"\n"
"font: 75 12pt\"Arial Narrow\";\n"
"}")
        self.lateral.setFrameShape(QFrame.StyledPanel)
        self.lateral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.lateral)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.lateral)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"margin-top:10px")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.Spanish = QPushButton(self.lateral)
        self.Spanish.setObjectName(u"Spanish")
        self.Spanish.setMinimumSize(QSize(0, 40))
        self.Spanish.setMaximumSize(QSize(16777215, 40))
        self.Spanish.setStyleSheet(u"QPushButton{\n"
"background-color: rgbrgb(33, 97, 140);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"front: 87 12pt \"Arial Black\";\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"imagenes/espa\u00f1a.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.Spanish.setIcon(icon1)
        self.Spanish.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.Spanish)

        self.English = QPushButton(self.lateral)
        self.English.setObjectName(u"English")
        self.English.setMinimumSize(QSize(0, 40))
        self.English.setMaximumSize(QSize(16777215, 40))
        self.English.setStyleSheet(u"QPushButton{\n"
"background-color: rgbrgb(33, 97, 140);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"front: 87 12pt \"Arial Black\";\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"imagenes/usa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.English.setIcon(icon2)
        self.English.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.English)

        self.English_2 = QPushButton(self.lateral)
        self.English_2.setObjectName(u"English_2")
        self.English_2.setMinimumSize(QSize(0, 40))
        self.English_2.setMaximumSize(QSize(16777215, 40))
        self.English_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgbrgb(33, 97, 140);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"front: 87 12pt \"Arial Black\";\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"imagenes/portugal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.English_2.setIcon(icon3)
        self.English_2.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.English_2)

        self.label_4 = QLabel(self.lateral)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.Radio1 = QRadioButton(self.lateral)
        self.Radio1.setObjectName(u"Radio1")
        self.Radio1.setStyleSheet(u"margin:15px auto;\n"
"font: 75 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout_3.addWidget(self.Radio1)

        self.Radio2 = QRadioButton(self.lateral)
        self.Radio2.setObjectName(u"Radio2")
        self.Radio2.setStyleSheet(u"margin:15px auto;\n"
"font: 75 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout_3.addWidget(self.Radio2)

        self.Radio3 = QRadioButton(self.lateral)
        self.Radio3.setObjectName(u"Radio3")
        self.Radio3.setStyleSheet(u"margin:15px auto;\n"
"font: 75 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout_3.addWidget(self.Radio3)

        self.verticalSpacer = QSpacerItem(20, 297, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label = QLabel(self.lateral)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.lateral)

        self.frame_contenedor = QFrame(self.frame_inferior)
        self.frame_contenedor.setObjectName(u"frame_contenedor")
        self.frame_contenedor.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_contenedor)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_contenedor)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.verticalLayout_4 = QVBoxLayout(self.page1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.imagenrobot = QPushButton(self.page1)
        self.imagenrobot.setObjectName(u"imagenrobot")
        self.imagenrobot.setStyleSheet(u"background-color: rgb(55, 150, 131);")
        icon4 = QIcon()
        icon4.addFile(u"../assets/robot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.imagenrobot.setIcon(icon4)
        self.imagenrobot.setIconSize(QSize(500, 500))

        self.verticalLayout_4.addWidget(self.imagenrobot)

        self.stackedWidget.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayout_5 = QVBoxLayout(self.page2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.MarcoDerecho = QFrame(self.page2)
        self.MarcoDerecho.setObjectName(u"MarcoDerecho")
        self.MarcoDerecho.setStyleSheet(u"background-color: rgb(46, 134, 193);")
        self.MarcoDerecho.setFrameShape(QFrame.StyledPanel)
        self.MarcoDerecho.setFrameShadow(QFrame.Raised)
        self.BotonBuscar = QPushButton(self.MarcoDerecho)
        self.BotonBuscar.setObjectName(u"BotonBuscar")
        self.BotonBuscar.setGeometry(QRect(520, 90, 74, 40))
        self.BotonBuscar.setMinimumSize(QSize(0, 40))
        self.BotonBuscar.setMaximumSize(QSize(16777215, 40))
        self.BotonBuscar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"front: 87 12pt \"Arial Black\";\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"imagenes/lupa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BotonBuscar.setIcon(icon5)
        self.Etiqueta = QLabel(self.MarcoDerecho)
        self.Etiqueta.setObjectName(u"Etiqueta")
        self.Etiqueta.setGeometry(QRect(90, 10, 491, 61))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.Etiqueta.setFont(font2)
        self.Etiqueta.setStyleSheet(u"QLabel{\n"
"border:0px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"front: 87 12pt \"Arial Black\";\n"
"}\n"
"")
        self.Etiqueta.setAlignment(Qt.AlignCenter)
        self.RespuestAN = QLabel(self.MarcoDerecho)
        self.RespuestAN.setObjectName(u"RespuestAN")
        self.RespuestAN.setGeometry(QRect(140, 130, 351, 21))
        self.RespuestAN.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.RespuestAN.setAlignment(Qt.AlignCenter)
        self.BuscarPalabra = QLineEdit(self.MarcoDerecho)
        self.BuscarPalabra.setObjectName(u"BuscarPalabra")
        self.BuscarPalabra.setGeometry(QRect(140, 100, 351, 21))
        self.BuscarPalabra.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame = QFrame(self.MarcoDerecho)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 160, 621, 421))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Q0 = QLabel(self.frame)
        self.Q0.setObjectName(u"Q0")
        self.Q0.setGeometry(QRect(65, 90, 31, 31))
        self.Q0.setAlignment(Qt.AlignCenter)
        self.Q1_2 = QLabel(self.frame)
        self.Q1_2.setObjectName(u"Q1_2")
        self.Q1_2.setGeometry(QRect(240, 50, 31, 31))
        self.Q1_2.setAlignment(Qt.AlignCenter)
        self.Q1 = QLabel(self.frame)
        self.Q1.setObjectName(u"Q1")
        self.Q1.setGeometry(QRect(270, 90, 31, 31))
        self.Q1.setAlignment(Qt.AlignCenter)
        self.Q2 = QLabel(self.frame)
        self.Q2.setObjectName(u"Q2")
        self.Q2.setGeometry(QRect(500, 90, 31, 31))
        self.Q2.setAlignment(Qt.AlignCenter)
        self.Q2_2 = QLabel(self.frame)
        self.Q2_2.setObjectName(u"Q2_2")
        self.Q2_2.setGeometry(QRect(390, 170, 31, 31))
        self.Q2_2.setAlignment(Qt.AlignCenter)
        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(-60, 120, 101, 31))
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"../imagenes/FirsTow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon6)
        self.pushButton_8.setIconSize(QSize(110, 50))
        self.Q0Q0 = QPushButton(self.frame)
        self.Q0Q0.setObjectName(u"Q0Q0")
        self.Q0Q0.setGeometry(QRect(60, 10, 81, 81))
        self.Q0Q0.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"imagenes/FirstNodo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Q0Q0.setIcon(icon7)
        self.Q0Q0.setIconSize(QSize(110, 200))
        self.Q0Q2 = QPushButton(self.frame)
        self.Q0Q2.setObjectName(u"Q0Q2")
        self.Q0Q2.setGeometry(QRect(160, 120, 101, 31))
        self.Q0Q2.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"imagenes/FirsTow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Q0Q2.setIcon(icon8)
        self.Q0Q2.setIconSize(QSize(110, 50))
        self.Q1Q2 = QPushButton(self.frame)
        self.Q1Q2.setObjectName(u"Q1Q2")
        self.Q1Q2.setGeometry(QRect(370, 120, 101, 31))
        self.Q1Q2.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}")
        self.Q1Q2.setIcon(icon8)
        self.Q1Q2.setIconSize(QSize(110, 50))
        self.Q1Q1 = QPushButton(self.frame)
        self.Q1Q1.setObjectName(u"Q1Q1")
        self.Q1Q1.setGeometry(QRect(270, 10, 81, 81))
        self.Q1Q1.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}")
        self.Q1Q1.setIcon(icon7)
        self.Q1Q1.setIconSize(QSize(110, 200))
        self.Q0Blanco = QPushButton(self.frame)
        self.Q0Blanco.setObjectName(u"Q0Blanco")
        self.Q0Blanco.setGeometry(QRect(60, 10, 81, 81))
        self.Q0Blanco.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}")
        self.Q0Blanco.setIcon(icon7)
        self.Q0Blanco.setIconSize(QSize(110, 200))
        self.Q1BLANCO = QPushButton(self.frame)
        self.Q1BLANCO.setObjectName(u"Q1BLANCO")
        self.Q1BLANCO.setGeometry(QRect(270, 10, 81, 81))
        self.Q1BLANCO.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}")
        self.Q1BLANCO.setIconSize(QSize(110, 200))
        self.Q0Q2_BLANCO = QPushButton(self.frame)
        self.Q0Q2_BLANCO.setObjectName(u"Q0Q2_BLANCO")
        self.Q0Q2_BLANCO.setGeometry(QRect(160, 120, 101, 31))
        self.Q0Q2_BLANCO.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}")
        self.Q0Q2_BLANCO.setIconSize(QSize(110, 50))
        self.Q1Q2_BLANCO = QPushButton(self.frame)
        self.Q1Q2_BLANCO.setObjectName(u"Q1Q2_BLANCO")
        self.Q1Q2_BLANCO.setGeometry(QRect(370, 120, 101, 31))
        self.Q1Q2_BLANCO.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}")
        self.Q1Q2_BLANCO.setIconSize(QSize(110, 50))
        self.pila1 = QPushButton(self.frame)
        self.pila1.setObjectName(u"pila1")
        self.pila1.setGeometry(QRect(60, 270, 61, 41))
        self.pila1.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"")
        self.pila2 = QPushButton(self.frame)
        self.pila2.setObjectName(u"pila2")
        self.pila2.setGeometry(QRect(120, 270, 61, 41))
        self.pila2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pila3 = QPushButton(self.frame)
        self.pila3.setObjectName(u"pila3")
        self.pila3.setGeometry(QRect(180, 270, 61, 41))
        self.pila3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pila4 = QPushButton(self.frame)
        self.pila4.setObjectName(u"pila4")
        self.pila4.setGeometry(QRect(300, 270, 61, 41))
        self.pila4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pila5 = QPushButton(self.frame)
        self.pila5.setObjectName(u"pila5")
        self.pila5.setGeometry(QRect(240, 270, 61, 41))
        self.pila5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pila6 = QPushButton(self.frame)
        self.pila6.setObjectName(u"pila6")
        self.pila6.setGeometry(QRect(360, 270, 61, 41))
        self.pila6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.pila7 = QPushButton(self.frame)
        self.pila7.setObjectName(u"pila7")
        self.pila7.setGeometry(QRect(420, 270, 61, 41))
        self.pila7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(480, 270, 61, 41))
        self.pushButton_9.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 0, 51, 21))
        self.lineEdit.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";\n"
"border: 0px")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 20, 51, 21))
        self.lineEdit_2.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";\n"
"border: 0px")
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 40, 51, 21))
        self.lineEdit_3.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";\n"
"border: 0px")
        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(10, 60, 51, 21))
        self.lineEdit_4.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";\n"
"border: 0px")
        self.lineEdit_5 = QLineEdit(self.frame)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(0, 90, 51, 21))
        self.lineEdit_5.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";\n"
"border: 0px")
        self.lineEdit_6 = QLineEdit(self.frame)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(0, 110, 51, 21))
        self.lineEdit_6.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";\n"
"border: 0px")
        self.lineEdit_7 = QLineEdit(self.frame)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(180, 100, 51, 21))
        self.lineEdit_7.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";\n"
"border: 0px")
        self.lineEdit_8 = QLineEdit(self.frame)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(180, 150, 51, 21))
        self.lineEdit_8.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";\n"
"border: 0px")
        self.lineEdit_10 = QLineEdit(self.frame)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(390, 150, 51, 21))
        self.lineEdit_10.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";\n"
"border: 0px")
        self.lineEdit_11 = QLineEdit(self.frame)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(350, 10, 51, 21))
        self.lineEdit_11.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";\n"
"border: 0px")
        self.lineEdit_12 = QLineEdit(self.frame)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(350, 30, 51, 21))
        self.lineEdit_12.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";\n"
"border: 0px")
        self.Q0Blanco.raise_()
        self.Q0Q0.raise_()
        self.Q1Q2_BLANCO.raise_()
        self.Q0Q2_BLANCO.raise_()
        self.Q1BLANCO.raise_()
        self.Q1Q1.raise_()
        self.Q1Q2.raise_()
        self.Q0Q2.raise_()
        self.Q0.raise_()
        self.Q1_2.raise_()
        self.Q1.raise_()
        self.Q2_2.raise_()
        self.Q2.raise_()
        self.pushButton_8.raise_()
        self.pila1.raise_()
        self.pila2.raise_()
        self.pila3.raise_()
        self.pila4.raise_()
        self.pila5.raise_()
        self.pila6.raise_()
        self.pila7.raise_()
        self.pushButton_9.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        self.lineEdit_7.raise_()
        self.lineEdit_8.raise_()
        self.lineEdit_10.raise_()
        self.lineEdit_11.raise_()
        self.lineEdit_12.raise_()

        self.verticalLayout_5.addWidget(self.MarcoDerecho)

        self.stackedWidget.addWidget(self.page2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_contenedor)


        self.verticalLayout.addWidget(self.frame_inferior)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Buscador.setText(QCoreApplication.translate("MainWindow", u"BUSCADOR", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"IDIOMA", None))
        self.Spanish.setText(QCoreApplication.translate("MainWindow", u"ESPA\u00d1OL", None))
        self.English.setText(QCoreApplication.translate("MainWindow", u" INGLES", None))
        self.English_2.setText(QCoreApplication.translate("MainWindow", u"PORTUGUES", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"VELOCIDADES", None))
        self.Radio1.setText(QCoreApplication.translate("MainWindow", u"    X 0.5", None))
        self.Radio2.setText(QCoreApplication.translate("MainWindow", u"    X 1", None))
        self.Radio3.setText(QCoreApplication.translate("MainWindow", u"    X 1.5", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Proyecto - Automata", None))
        self.imagenrobot.setText("")
        self.BotonBuscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.Etiqueta.setText(QCoreApplication.translate("MainWindow", u"Automata de pila | palindromo", None))
        self.RespuestAN.setText("")
        self.BuscarPalabra.setPlaceholderText("")
        self.Q0.setText(QCoreApplication.translate("MainWindow", u" Q0", None))
        self.Q1_2.setText("")
        self.Q1.setText(QCoreApplication.translate("MainWindow", u" Q1", None))
        self.Q2.setText(QCoreApplication.translate("MainWindow", u" Q2", None))
        self.Q2_2.setText("")
        self.pushButton_8.setText("")
        self.Q0Q0.setText("")
        self.Q0Q2.setText("")
        self.Q1Q2.setText("")
        self.Q1Q1.setText("")
        self.Q0Blanco.setText("")
        self.Q1BLANCO.setText("")
        self.Q0Q2_BLANCO.setText("")
        self.Q1Q2_BLANCO.setText("")
        self.pila1.setText("")
        self.pila2.setText("")
        self.pila3.setText("")
        self.pila4.setText("")
        self.pila5.setText("")
        self.pila6.setText("")
        self.pila7.setText("")
        self.pushButton_9.setText("")
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"b,b/bb", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"a,b/ba", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"b,a/ab", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"a,a/aa", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"b,#/#b", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"a,#/#a", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"b,b/\u03bb", None))
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"a,a/\u03bb", None))
        self.lineEdit_10.setText(QCoreApplication.translate("MainWindow", u"\u03bb,#/#", None))
        self.lineEdit_11.setText(QCoreApplication.translate("MainWindow", u"b,b/\u03bb", None))
        self.lineEdit_12.setText(QCoreApplication.translate("MainWindow", u"a,a/\u03bb", None))
    # retranslateUi

