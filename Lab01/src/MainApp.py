
from PyQt5 import QtCore, QtWidgets

from AboutDialog import AboutDialog
from AdminWindow import AdminWindow
from MainWindow import MainWindow


class MainApp(QtWidgets.QApplication):
	
	def __init__(self):
		super().__init__([])

		self.mainWindow = MainWindow()
		self.aboutDialog = AboutDialog(self.mainWindow)
		self.adminWindow = AdminWindow(self.mainWindow)

		self.mainWindow.ui.actionAbout.triggered.connect(self.aboutDialog.show)
		self.mainWindow.ui.actionExit.triggered.connect(self.exit)
		self.mainWindow.ui.buttonBox.rejected.connect(self.exit)
		
		self.mainWindow.noMoreAttempts.connect(self.exit)
		self.mainWindow.onAdminEnter.connect(self.adminWindow.enter)

		self.adminWindow.onExit.connect(self.mainWindow.updateUsers)


	def start(self):
		self.mainWindow.show()
		super().exec()

	def exit(self):
		self.mainWindow.close()
		super().exit()
