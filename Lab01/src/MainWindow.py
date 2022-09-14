

from PyQt5 import QtWidgets, QtCore, QtGui


from Users import Users
from UserAccount import UserAccount

from forms.mainWindow import Ui_LoginWindow

class MainWindow(QtWidgets.QMainWindow):

	noMoreAttempts = QtCore.pyqtSignal()
	onAdminEnter = QtCore.pyqtSignal(UserAccount)
	onUserEnter = QtCore.pyqtSignal(UserAccount)

	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)

		self.ui = Ui_LoginWindow()
		self.ui.setupUi(self)

		self.leftAttempts = 3

		self.users = Users('users.json')

		self.messageBox = QtWidgets.QMessageBox(self)

		self.ui.buttonBox.accepted.connect(self.checkValidInput)


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



	def processNoAttemptsLeft(self):
		# close after 3 attempts
		self.messageBox.setText(f'No attempts left, closing...')
		self.messageBox.show()
		self.messageBox.finished.connect(self.noMoreAttempts.emit)



	def processNoLogin(self):
		self.leftAttempts -= 1
		self.messageBox.setText(f'No Login, retry! {self.leftAttempts} attempts left')
		self.messageBox.show()



	def processNoPassword(self, enteredLogin, enteredPassword):
		acc = self.users.getAccount(enteredLogin, enteredPassword)
		if acc and acc.isAdmin():
			self.onAdminEnter.emit(acc)
		else:
			self.leftAttempts -= 1
			self.messageBox.setText(f'No password, retry! {self.leftAttempts} attempts left')
			self.messageBox.show()




	def processValidInput(self, enteredLogin, enteredPassword):
		acc = self.users.getAccount(enteredLogin, enteredPassword)
		print(f'Got account: {acc}')
		if acc is None:
			self.leftAttempts -= 1
			self.messageBox.setText(f'Wrong login or password, attempts left: {self.leftAttempts}')
			self.messageBox.show()
		elif acc.isAdmin(): self.onAdminEnter.emit(acc)
		else:
			self.onUserEnter.emit(acc)


	def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
		self.users.save()



	
