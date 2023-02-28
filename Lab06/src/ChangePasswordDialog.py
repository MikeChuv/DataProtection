from PyQt5 import QtWidgets, QtCore
from UserAccount import UserAccount

from ui.ui_passwordChangeDialog import Ui_ChangePasswordDialog




class ChangePasswordDialog(QtWidgets.QDialog):

	onPasswordChanged = QtCore.pyqtSignal(UserAccount)

	def __init__(self, parent):
		super(ChangePasswordDialog, self).__init__(parent)

		self.ui = Ui_ChangePasswordDialog()
		self.ui.setupUi(self)

		self.messageBox = QtWidgets.QMessageBox(self)

		self.ui.buttonBox.accepted.connect(self.changePassword)
		


	def changePassword(self):
		if self.ui.oldPasswordEdit.text() == self._currentUser.password:
			newPass = self.ui.newPasswordEdit.text()
			if newPass == self.ui.confirmNewPasswordEdit.text():
				if newPass == '':
					self.messageBox.setText(f'Empty password is not allowed!')
					self.messageBox.show()
				elif (self._currentUser.hasPasswordRestriction
					and self.passwordFits(newPass)) \
					or not self._currentUser.hasPasswordRestriction:

					self._currentUser.password = newPass
					self.messageBox.setText(f'Password changed')
					self.messageBox.show()
					self.onPasswordChanged.emit(self._currentUser)
					self.close()
				else:
					self.messageBox.setText(f'You have to follow: letters, operators and digits!')
					self.messageBox.show()
			else:
				self.messageBox.setText(f'Confirmation failed, try again!')
				self.messageBox.show()
		else:
			self.messageBox.setText(f'Wrong password!')
			self.messageBox.show()




	def passwordFits(self, password : str):
		# Вариант 48: Чередование букв, знаков арифметических операций, цифр.
		letterFlag = False
		opFlag = False
		digitFlag = False
		for ch in password:
			if ch.isalpha(): letterFlag = True
			elif ch in ('+', '-', '*', '/') and letterFlag: opFlag = True
			elif ch.isdigit() and opFlag: digitFlag = True;
		if letterFlag and opFlag and digitFlag: return True
		else: return False

		


	@QtCore.pyqtSlot(UserAccount)
	def enter(self, account : UserAccount):
		self._currentUser = account
		self.show()