# -*- coding: utf-8 -*-

# PyQt5
from PyQt5 import QtWidgets

# GUI
import Main_Window.main_window as main_window
from message_box import MessageBox

# Другое
from cryptography.fernet import Fernet, InvalidToken
import methods as Method

# Главное окно
class MainWindow(Method.CreateMainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = main_window.Ui_MainWindow()
		self.ui.setupUi(self)

		# Все нужные переменные
		self.program_data = {
			'Crypto_key': None,
			'Files': None
		}

		# Оброботчик основных кнопок
		self.ui.CreateCryptoKeyButton.clicked.connect(self.create_crypto_key_button)
		self.ui.AddCryptoKeyButton.clicked.connect(self.add_crypto_key_button)
		self.ui.AddFilesButton.clicked.connect(self.add_files_button)
		self.ui.RemoveFilesButton.clicked.connect(self.remove_files_button)
		self.ui.EncryptFilesButton.clicked.connect(self.encrypt_files_button)
		self.ui.DecipherFilesButton.clicked.connect(self.decipher_files_button)

		# Обработчики кнопок с панели
		self.ui.CloseWindowButton.clicked.connect(lambda: self.close())
		self.ui.MinimizeWindowButton.clicked.connect(lambda: self.showMinimized())

	# Декоратор
	# ==================================================================
	def check_program_data(func):
		def wrapper(self, message_box, button_text):
			message_box.close()

			if button_text == 'Да':
				if self.program_data['Crypto_key'] != None:
					if self.program_data['Files'] != None:
						with open(self.program_data['Crypto_key'], 'rb') as f:
							data = f.read()
							crypto_key = Fernet(data)
						func(self, crypto_key)
					else:
						MessageBox(text='Сначала добавьте файл(ы), которые вы хотите зашифровать!', button_1='Окей')
				else:
					MessageBox(text='Сначала добавьте ключ шифрования!', button_1='Окей')
		wrapper.__name__ = func.__name__
		return wrapper
	# ==================================================================

	# Логика для основных кнопок
	# ==================================================================
	def create_crypto_key_button(self):
		message_box = MessageBox(text='Вы точно хотите создать ключ шифрования?', button_1='Да', button_2='Нет')
		message_box.message_box.signalButton.connect(lambda text: self.create_crypto_key(message_box.message_box, text))

	def add_crypto_key_button(self):
		data = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите ключ шифрования', filter=("Ключ шифрования (*.key)"))
		if data[0] != '':
			self.program_data['Crypto_key'] = data[0]
			if self.ui.AddCryptoKeyButton.text() == 'Заменить ключ шифрования':
				self.update_program_log(recent_actions='Успешно заменён ключ шифрования')
			else:
				self.update_program_log(recent_actions='Успешно добавлен ключ шифрования')
			self.ui.AddCryptoKeyButton.setText('Заменить ключ шифрования')

	def add_files_button(self):
		files = QtWidgets.QFileDialog.getOpenFileNames(self)
		if files[0] != []:
			self.program_data['Files'] = files[0]
			if self.ui.AddFilesButton.text() == 'Заменить файл(ы)':
				self.update_program_log(recent_actions='Успешная замена файл(а/ов) для шифрования/расшифрования')
			else:
				self.update_program_log(recent_actions='Успешное добавление файл(а/ов) для шифрования/расшифрования')
			self.ui.AddFilesButton.setText('Заменить файл(ы)')

	def remove_files_button(self):
		if self.program_data['Files'] != None:
			message_box = MessageBox(text='Вы точно хотите удалить файл(ы) из данных?', button_1='Да', button_2='Нет')
			message_box.message_box.signalButton.connect(lambda button_text: self.remove_files(message_box.message_box, button_text))
		else:
			MessageBox(text='Сначала добавьте файл(ы) в данные программы.', button_1='Окей')

	def encrypt_files_button(self):
		message_box = MessageBox(text='Вы точно хотите зашифровать файл(ы)?', button_1='Да', button_2='Нет')
		message_box.message_box.signalButton.connect(lambda button_text: self.encrypt_files(message_box.message_box, button_text))

	def decipher_files_button(self):
		message_box = MessageBox(text='Вы точно хотите расшифровать файл(ы)?', button_1='Да', button_2='Нет')
		message_box.message_box.signalButton.connect(lambda button_text: self.decipher_files(message_box.message_box, button_text))
	# ==================================================================

	# Обычные функции
	# ==================================================================
	def update_program_log(self, recent_actions: str='Отсутствует'):
		text='Ключ шифрования:\n'
		if self.program_data['Crypto_key'] != None:
			text += f"  • {self.program_data['Crypto_key']}\n\n"
		else:
			text += '  • Отсутствует\n\n'

		text += 'Файл(ы) для шифрования/расшифрования:\n'
		if self.program_data['Files'] != None:
			for file in self.program_data['Files']:
				text += f"  • {file}\n"
		else:
			text += '  • Отсутствует\n'

		text += f"""
Последние действие:
  • {recent_actions}"""

		self.ui.ProgramLogsPlainTextEdit.setPlainText(text)

	def create_crypto_key(self, message_box, button_text: str):
		message_box.close()

		if button_text == 'Да':
			data = QtWidgets.QFileDialog.getSaveFileName(self, 'Сохраните ключ шифрования', filter=("Ключ шифрования (*.key)"))
			if data[0] != '':
				crypto_key = Fernet.generate_key()
				with open(data[0], 'wb') as key_file:
					key_file.write(crypto_key)

				self.update_program_log(recent_actions='Успешное создание ключа шифрования.')
				MessageBox(text='Вы успешно создали ключ шифрования.', button_1='Окей')

	def remove_files(self, message_box, button_text: str):
		message_box.close()

		if button_text == 'Да':
			self.program_data['Files'] = None
			self.ui.AddFilesButton.setText('Добавить файл(ы)')
			self.update_program_log('Успешное удаление фай(а/лов) для шифрования/расшифрования из данных программы.')
			MessageBox(text='Вы успешно удалили файл(ы) из данных программы.', button_1='Окей')

	@check_program_data
	def encrypt_files(self, crypto_key: Fernet):
		for file in self.program_data['Files']:
			with open(file, 'rb') as f:
				data = f.read()
				data = crypto_key.encrypt(data)
			with open(file, 'wb') as f:
				f.write(data)

		self.update_program_log('Успешное шифрование файл(а/ов).')
		MessageBox(text='Вы успешно зашифровали файл(ы).', button_1='Окей')

	@check_program_data
	def decipher_files(self, crypto_key: Fernet):
		try:
			for file in self.program_data['Files']:
				with open(file, 'rb') as f:
					data = f.read()
					data = crypto_key.decrypt(data)
				with open(file, 'wb') as f:
					f.write(data)

			self.update_program_log('Успешное расшифрование файл(а/ов).')
			MessageBox(text='Вы успешно расшифровали файл(ы).', button_1='Окей')
		except InvalidToken:
			MessageBox(text=f'Файл(ы) уже расшифрован!', button_1='Окей')
	# ==================================================================