
from PyQt5 import QtCore, QtWidgets




from MainWindow import MainWindow
from AdminWindow import AdminWindow
from AboutDialog import AboutDialog
from NewUserDialog import NewUserDialog
from ChangePasswordDialog import ChangePasswordDialog


from Admin import Admin
from Users import Users


class MainApp(QtWidgets.QApplication):
	
	def __init__(self):
		super().__init__([])

		self.mainWindow = MainWindow()
		self.aboutDialog = AboutDialog(self.mainWindow)
		self.adminWindow = AdminWindow(self.mainWindow)
		self.newUserDialog = NewUserDialog(self.mainWindow)
		self.changePasswordDialog = ChangePasswordDialog(self.mainWindow)


		self.mainWindow.ui.actionAbout.triggered.connect(self.aboutDialog.show)
		self.mainWindow.ui.actionExit.triggered.connect(super().exit)

		self.mainWindow.ui.buttonBox.rejected.connect(super().exit)

		self.mainWindow.noMoreAttempts.connect(super().exit)
		self.mainWindow.onAdminEnter.connect(self.adminWindow.enter)
		self.mainWindow.onUserEnter.connect(self.changePasswordDialog.enter)


	def start(self):
		self.mainWindow.show()
		super().exec()

