# -*- coding: utf-8 -*-

# PyQt5
from PyQt5 import QtWidgets

# GUI
from main_window import MainWindow

# Другие
import sys

# Запуск GUI
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	myapp = MainWindow()
	myapp.show()
	sys.exit(app.exec_())