# -*- coding: utf-8 -*-

# PyQt5
from PyQt5 import QtCore, QtWidgets

# GUI
import Main_Window.main_window as main_window
from message_box import MessageBox

# Другое
from cryptography.fernet import Fernet, InvalidToken

# Главное окно
class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, parent = None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = main_window.Ui_MainWindow()
		self.ui.setupUi(self)

		# Отключаем стандартные границы окна программы
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.center()

		# Все нужные переменные
		self.program_info = {
			'Crypto_key': None,
			'Files': None
		}

		# Оброботчик основных кнопок
		self.ui.CreateCryptoKeyButton.clicked.connect(self.create_crypto_key_button)
		self.ui.AddCryptoKeyButton.clicked.connect(self.add_crypto_key)
		self.ui.AddFilesButton.clicked.connect(self.add_files)
		self.ui.RemoveFilesButton.clicked.connect(self.remove_files_button)
		self.ui.EncryptFilesButton.clicked.connect(self.encrypt_files_button)
		self.ui.DecipherFilesButton.clicked.connect(self.decipher_files_button)

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

	# Логика для основных кнопок
	# ==================================================================
	def create_crypto_key_button(self):
		message_box = MessageBox(text = 'Вы точно хотите создать ключ шифрования?', button_1 = 'Да', button_2 = 'Нет')
		message_box.message_box.signalButton.connect(lambda text: self.create_crypto_key(message_box.message_box, text))

	def add_crypto_key(self):
		data = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите ключ шифрования', filter = ("Ключ шифрования (*.key)"))
		if data[0] != '':
			self.program_info['Crypto_key'] = data[0]
			self.update_program_logs(recent_actions = 'Добавление ключа доступа')

	def add_files(self):
		files = QtWidgets.QFileDialog.getOpenFileNames(self)
		if files[0] != []:
			self.program_info['Files'] = files[0]
			self.update_program_logs(recent_actions = 'Успешное добавление файлов для шифрования/расшифрования')

	def remove_files_button(self):
		message_box = MessageBox(text = 'Вы точно хотите удалить файл(ы) для шифрования/расшифрования из данных программы?', button_1 = 'Да', button_2 = 'Нет')
		message_box.message_box.signalButton.connect(lambda text: self.remove_files(message_box.message_box, text))

	def encrypt_files_button(self):
		message_box = MessageBox(text = 'Вы точно хотите зашифровать файл(ы)?', button_1 = 'Да', button_2 = 'Нет')
		message_box.message_box.signalButton.connect(lambda text: self.encrypt_files(message_box.message_box, text))

	def decipher_files_button(self):
		message_box = MessageBox(text = 'Вы точно хотите расшифровать файл(ы)?', button_1 = 'Да', button_2 = 'Нет')
		message_box.message_box.signalButton.connect(lambda text: self.decipher_files(message_box.message_box, text))
	# ==================================================================

	# Обычные функции
	# ==================================================================
	def update_program_logs(self, recent_actions = 'Отсутствует'):
		text = 'Ключ шифрования:\n'
		if self.program_info['Crypto_key'] != None:
			text += f"  • {self.program_info['Crypto_key']}\n\n"
		else:
			text += '  • Отсутствует\n\n'

		text += 'Файл(ы) для шифрования/расшифрования:\n'
		if self.program_info['Files'] != None:
			for file in self.program_info['Files']:
				text += f"  • {file}\n"
		else:
			text += '  • Отсутствует\n'

		text += f"""
Последние действие:
  • {recent_actions}"""

		self.ui.ProgramLogsPlainTextEdit.setPlainText(text)

	def create_crypto_key(self, message_box, text):
		message_box.close()

		if text == 'Да':
			data = QtWidgets.QFileDialog.getSaveFileName(self, 'Сохраните ключ шифрования', filter = ("Ключ шифрования (*.key)"))
			if data[0] != '':
				key = Fernet.generate_key()
				with open(data[0], 'wb') as key_file:
					key_file.write(key)

				self.update_program_logs(recent_actions = 'Успешное создание ключа шифрования')
				MessageBox(text = 'Вы успешно создали ключ шифрования.', button_1 = 'Окей')

	def remove_files(self, message_box, text):
		message_box.close()

		if text == 'Да':
			self.program_info['Files'] = None
			self.update_program_logs('Успешное удаление фай(а/лов) для шифрования/расшифрования из данных программы')
			MessageBox(text = 'Вы успешно удалили файл(ы) для шифрования/расшифрования из данных программы.', button_1 = 'Окей')

	def encrypt_files(self, message_box, text):
		message_box.close()

		if text == 'Да':
			if self.program_info['Crypto_key'] != None:
				with open(self.program_info['Crypto_key'], 'rb') as file:
					data = file.read()
					crypto_key =  Fernet(data)
				for file in self.program_info['Files']:
					with open(file, 'rb') as f:
						data = f.read()
						data = crypto_key.encrypt(f.read())
					with open(file, 'wb') as f:
						f.write(data)

				MessageBox(text = 'Вы успешно зашифровали файл(ы).', button_1 = 'Окей')
				self.update_program_logs('Успешное шифрование файл(а/ов).')
			else:
				MessageBox(text = 'Сначала добавьте ключ шифрования!', button_1 = 'Окей')

	def decipher_files(self, message_box, text):
		message_box.close()

		if text == 'Да':
			if self.program_info['Crypto_key'] != None:
				with open(self.program_info['Crypto_key'], 'rb') as file:
					crypto_key =  Fernet(file.read())
				try:
					for file in self.program_info['Files']:
						with open(file, 'rb') as f:
							data = f.read()
							data = crypto_key.decrypt(f.read())
						with open(file, 'wb') as f:
							f.write(data)

					MessageBox(text = 'Вы успешно расшифровали файл(ы).', button_1 = 'Окей')
					self.update_program_logs('Успешное расшифрование файл(а/ов).')
				except InvalidToken:
					MessageBox(text = f'Файл "{file}" уже расшифрован!', button_1 = 'Окей')
			else:
				MessageBox(text = 'Сначала добавьте ключ шифрования!', button_1 = 'Окей')
	# ==================================================================