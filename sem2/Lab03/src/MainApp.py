
from PyQt5 import QtCore, QtWidgets

from MainWindow import MainWindow


class MainApp(QtWidgets.QApplication):
	
	def __init__(self):
		super().__init__([])

		self.mainWindow = MainWindow()


	def start(self):
		try:
			self.mainWindow.show()
		except:
			self.mainWindow.users.save(self.mainWindow.usersPath)
		super().exec()
