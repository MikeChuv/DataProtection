
from PyQt5 import QtWidgets, QtCore, QtGui

from ChangePasswordDialog import ChangePasswordDialog
from UserAccount import UserAccount
from Users import Users

from forms.mainWindow import Ui_LoginWindow



class MainWindow(QtWidgets.QMainWindow):

	noMoreAttempts = QtCore.pyqtSignal()
	onAdminEnter = QtCore.pyqtSignal(UserAccount, Users)
	onUserEnter = QtCore.pyqtSignal(UserAccount)
	users = None

	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)

		self.ui = Ui_LoginWindow()
		self.ui.setupUi(self)

		self.leftAttempts = 3

		self.changePasswordDialog = ChangePasswordDialog(self)
		self.messageBox = QtWidgets.QMessageBox(self)

		self.ui.buttonBox.accepted.connect(self.checkValidInput)
		self.onUserEnter.connect(self.setCurrentUser)
		self.onUserEnter.connect(self.changePasswordDialog.enter)
		self.changePasswordDialog.onPasswordChanged.connect(self.updateCurrentUser)


	@QtCore.pyqtSlot()
	def checkValidInput(self):
		enteredLogin = self.ui.loginEdit.text()
		enteredPassword = self.ui.passwordEdit.text()
		if self.leftAttempts <= 1:
			self.processNoAttemptsLeft()
		elif not enteredLogin:
			self.processNoLogin()
		elif not enteredPassword:
			self.processNoPassword(enteredLogin, enteredPassword)
		else:
			# input is valid
			self.processValidInput(enteredLogin, enteredPassword)


	def loadUsers(self, k : bytes):
		self.users = Users('users.bin', k)

	@QtCore.pyqtSlot(Users)
	def updateUsers(self, users : Users):
		self.users = users



	@QtCore.pyqtSlot(UserAccount)
	def setCurrentUser(self, user : UserAccount):
		self._currentUser = user


	@QtCore.pyqtSlot(UserAccount)
	def updateCurrentUser(self, user : UserAccount):
		self.users.updateAccount(self._currentUser, user)


	def processNoAttemptsLeft(self):
		# close after 3 attempts
		self.messageBox.setText(f'No attempts left, closing...')
		self.messageBox.show()
		self.messageBox.finished.connect(self.noMoreAttempts.emit)



	def processNoLogin(self):
		self.leftAttempts -= 1
		self.messageBox.setText(f'No Login, retry! {self.leftAttempts} attempts left')
		self.messageBox.show()
		self.ui.passwordEdit.clear()



	def processNoPassword(self, enteredLogin : str, enteredPassword : str):
		acc = self.users.getAccount(enteredLogin, enteredPassword)
		if acc and acc.isAdmin():
			self.onAdminEnter.emit(acc, self.users)
		elif acc:
			if not acc.blocked:
				self.onUserEnter.emit(acc)
			else:
				self.messageBox.setText(f'Your account is blocked by admin!')
				self.messageBox.show()
		else:
			self.leftAttempts -= 1
			self.messageBox.setText(f'No password, retry! {self.leftAttempts} attempts left')
			self.messageBox.show()
		self.ui.loginEdit.clear()
		self.ui.passwordEdit.clear()




	def processValidInput(self, enteredLogin : str, enteredPassword : str):
		acc = self.users.getAccount(enteredLogin, enteredPassword)
		if acc and acc.isAdmin():
			self.onAdminEnter.emit(acc, self.users)
		elif acc:
			if not acc.blocked:
				self.onUserEnter.emit(acc)
			else:
				self.messageBox.setText(f'Your account is blocked by admin!')
				self.messageBox.show()
		else:
			self.leftAttempts -= 1
			self.messageBox.setText(f'Wrong login or password, attempts left: {self.leftAttempts}')
			self.messageBox.show()
		self.ui.loginEdit.clear()
		self.ui.passwordEdit.clear()



	def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
		self.users.save()





	
