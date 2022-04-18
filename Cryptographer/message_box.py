# -*- coding: utf-8 -*-

# PyQt5
from PyQt5 import QtCore,	QtGui, QtWidgets

# GUI
import Message_Box.message_box as message_box

class QMessageBox(QtWidgets.QMainWindow):
	signalButton = QtCore.pyqtSignal(str)

	def __init__(self, text, button_1, button_2, parent=None):
		super().__init__(parent, QtCore.Qt.Window)
		self.ui = message_box.Ui_Form()
		self.ui.setupUi(self)
		self.setWindowModality(2)

		# Отключаем стандартные границы окна программы
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.center()

		# Создание всех нужных переменных
		_translate = QtCore.QCoreApplication.translate

		buttons_font = QtGui.QFont()
		buttons_font.setPointSize(11)
		buttons_font.setBold(True)
		buttons_font.setWeight(75)

		buttons_style = """
QPushButton{
	color: white;
	border-radius: 8px;
	background-color: #C104A5;
}

QPushButton:hover{
	background-color: #CF03B0;
}

QPushButton:pressed{
	background-color: #AF0396;
}
"""

		self.ui.PlainTextEdit.setPlainText(text)
		if button_1 != None and button_2 != None:
			self.Button_1 = QtWidgets.QPushButton(self.ui.Window)
			self.Button_1.setGeometry(QtCore.QRect(20, 100, 161, 41))
			self.Button_1.setFont(buttons_font)
			self.Button_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
			self.Button_1.setStyleSheet(buttons_style)

			self.Button_2 = QtWidgets.QPushButton(self.ui.Window)
			self.Button_2.setGeometry(QtCore.QRect(190, 100, 161, 41))
			self.Button_2.setFont(buttons_font)
			self.Button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
			self.Button_2.setStyleSheet(buttons_style)

			self.Button_1.setText(_translate('Form', button_1))
			self.Button_2.setText(_translate('Form', button_2))

			self.Button_1.clicked.connect(lambda: self.signalButton.emit(button_1))
			self.Button_2.clicked.connect(lambda: self.signalButton.emit(button_2))
		elif button_1 != None:
			self.Button_1 = QtWidgets.QPushButton(self.ui.Window)
			self.Button_1.setGeometry(QtCore.QRect(110, 100, 161, 41))
			self.Button_1.setFont(buttons_font)
			self.Button_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
			self.Button_1.setStyleSheet(buttons_style)

			self.Button_1.setText(_translate('Form', button_1))
			self.Button_1.clicked.connect(lambda: self.signalButton.emit(button_1))
		elif button_2 != None:
			self.Button_2 = QtWidgets.QPushButton(self.ui.Window)
			self.Button_2.setGeometry(QtCore.QRect(110, 100, 161, 41))
			self.Button_2.setFont(buttons_font)
			self.Button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
			self.Button_2.setStyleSheet(buttons_style)

			self.Button_2.setText(_translate('Form', button_2))
			self.Button_2.clicked.connect(lambda: self.signalButton.emit(button_2))

		# Обработчики кнопок с панели
		self.ui.CloseWindowButton.clicked.connect(lambda: self.close())
		self.ui.MinimizeWindowButton.clicked.connect(lambda: self.showMinimized())

	# Перетаскивание безрамочного окна
	# ==================================================================
	def center(self):
		qr = self.frameGeometry()
		cp = QtWidgets.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def mousePressEvent(self, event):
		self.oldPos = event.globalPos()

	def mouseMoveEvent(self, event):
		try:
			delta = QtCore.QPoint(event.globalPos() - self.oldPos)
			self.move(self.x() + delta.x(), self.y() + delta.y())
			self.oldPos = event.globalPos()
		except AttributeError:
			pass
	# ==================================================================

class MessageBox:
	def __init__(self, text='', button_1=None, button_2=None):
		self.message_box = QMessageBox(text, button_1, button_2)
		self.message_box.signalButton.connect(lambda: self.message_box.close())
		self.message_box.show()