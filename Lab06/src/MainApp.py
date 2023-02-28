
from PyQt5 import QtCore, QtWidgets

from AboutDialog import AboutDialog
from AdminWindow import AdminWindow
from MainWindow import MainWindow
from DecryptUsersDialog import DecryptUsersDialog
from RegPartitionEnterDialog import RegPartitionEnterDialog


class MainApp(QtWidgets.QApplication):
	
	def __init__(self):
		super().__init__([])

		self.mainWindow = MainWindow()
		self.aboutDialog = AboutDialog(self.mainWindow)
		self.adminWindow = AdminWindow(self.mainWindow)
		self.regPartitionEnterDialog = RegPartitionEnterDialog()
		self.decryptUsersDialog = DecryptUsersDialog()
		self.messageBox = QtWidgets.QMessageBox()
		self.messageBox.setWindowTitle('Error')

		self.mainWindow.ui.actionAbout.triggered.connect(self.aboutDialog.show)
		self.mainWindow.ui.actionExit.triggered.connect(self.exit)
		self.mainWindow.ui.buttonBox.rejected.connect(self.exit)
		
		self.mainWindow.noMoreAttempts.connect(self.exit)
		self.mainWindow.onAdminEnter.connect(self.adminWindow.enter)

		self.adminWindow.onExit.connect(self.mainWindow.updateUsers)

		self.regPartitionEnterDialog.onKeyChecked.connect(self.toDecryptState)
		self.decryptUsersDialog.onPasswordEntered.connect(self.loadUsers)

	def start(self):
		self.regPartitionEnterDialog.show()
		super().exec()

	def toDecryptState(self):
		self.decryptUsersDialog.show()

	@QtCore.pyqtSlot(bytes)
	def loadUsers(self, k : bytes):
		try:
			self.mainWindow.loadUsers(k)
			del self.decryptUsersDialog
			self.mainWindow.show()
		except Exception as e:
			self.messageBox.setText(str(e))
			self.messageBox.show()
			del self.decryptUsersDialog

	def exit(self):
		self.mainWindow.close()
		super().exit()
