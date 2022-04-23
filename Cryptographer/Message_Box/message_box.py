# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'message_box.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(491, 151)
        self.Window = QtWidgets.QFrame(Form)
        self.Window.setGeometry(QtCore.QRect(10, 10, 471, 131))
        self.Window.setStyleSheet("QFrame{\n"
"    border-radius: 7px;\n"
"    background-color: #1B1D23;\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"    border: none;\n"
"    background: #595F76;\n"
"    width: 15px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical{    \n"
"    background-color: #494E61;\n"
"    min-height: 30px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: #D5006A;\n"
"}\n"
"QScrollBar::handle:vertical:pressed{    \n"
"    background-color: #B9005C;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"    border: none;\n"
"    background-color: #3A3F50;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover{    \n"
"    background-color: #D5006A;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{    \n"
"    background-color: #B9005C;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"    border: none;\n"
"    background-color: #3A3F50;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover{    \n"
"    background-color: #D5006A;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{    \n"
"    background-color: #B9005C;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal{\n"
"    border: none;\n"
"    background: #595F76;\n"
"    height: 15px;\n"
"    margin: 0px 15 0px 15;\n"
"    border-radius: opx;\n"
" }\n"
"\n"
"QScrollBar::handle:horizontal{    \n"
"    background-color: #494E61;\n"
"    min-width: 30px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover{    \n"
"    background-color: #D5006A;\n"
"}\n"
"QScrollBar::handle:horizontal:pressed{    \n"
"    background-color: #B9005C;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal{\n"
"    border: none;\n"
"    background-color: #3A3F50;\n"
"    width: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover{    \n"
"    background-color:#D5006A;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed{    \n"
"    background-color: #B9005C;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"    border: none;\n"
"    background-color: #3A3F50;\n"
"    width: 15px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover{    \n"
"    background-color: #D5006A;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed{    \n"
"    background-color: #B9005C;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal{\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{\n"
"    background: none;\n"
"}")
        self.Window.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Window.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Window.setObjectName("Window")
        self.WindowFrame = QtWidgets.QFrame(self.Window)
        self.WindowFrame.setGeometry(QtCore.QRect(0, 0, 471, 31))
        self.WindowFrame.setStyleSheet("QFrame{\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    background-color: #2C313C;\n"
"}")
        self.WindowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.WindowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.WindowFrame.setObjectName("WindowFrame")
        self.CloseWindowButton = QtWidgets.QPushButton(self.WindowFrame)
        self.CloseWindowButton.setGeometry(QtCore.QRect(431, 0, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.CloseWindowButton.setFont(font)
        self.CloseWindowButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CloseWindowButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border: none;\n"
"    border-top-right-radius: 7px;\n"
"    background-color: #2C313C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #45494D;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: #EA2F4E;\n"
"}")
        self.CloseWindowButton.setObjectName("CloseWindowButton")
        self.MinimizeWindowButton = QtWidgets.QPushButton(self.WindowFrame)
        self.MinimizeWindowButton.setGeometry(QtCore.QRect(390, 0, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.MinimizeWindowButton.setFont(font)
        self.MinimizeWindowButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MinimizeWindowButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border: none;\n"
"    background-color: #2C313C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #45494D;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: #EA2F4E;\n"
"}")
        self.MinimizeWindowButton.setDefault(False)
        self.MinimizeWindowButton.setObjectName("MinimizeWindowButton")
        self.Label = QtWidgets.QLabel(self.Window)
        self.Label.setGeometry(QtCore.QRect(20, 40, 431, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label.sizePolicy().hasHeightForWidth())
        self.Label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Label.setFont(font)
        self.Label.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.Label.setText("")
        self.Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Label.setObjectName("Label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.CloseWindowButton.setText(_translate("Form", "X"))
        self.MinimizeWindowButton.setText(_translate("Form", "_"))
