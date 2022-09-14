from PyQt5 import QtWidgets, QtCore
from UserAccount import UserAccount
from MainWindow import MainWindow

from forms.passwordChangeDialogWindow import Ui_ChangePasswordDialog

class ChangePasswordDialog(QtWidgets.QDialog):

	onPasswordChanged = QtCore.pyqtSignal(UserAccount)

	def __init__(self, parent):
		super(ChangePasswordDialog, self).__init__(parent)

		self.ui = Ui_ChangePasswordDialog()
		self.ui.setupUi(self)

		self.messageBox = QtWidgets.QMessageBox(self)

		self.ui.buttonBox.accepted.connect(self.changePassword)
		


	# add password change -- emit signal with UserAccount
	def changePassword(self):
		if self.ui.oldPasswordEdit.text() == self._currentUser.password:
			newPass = self.ui.newPasswordEdit.text()
			if newPass == self.ui.confirmNewPasswordEdit.text():
				self._currentUser.password = newPass
				self.messageBox.setText(f'Password changed')
				self.messageBox.show()
				self.onPasswordChanged.emit(self._currentUser)
				self.close()
			else:
				self.messageBox.setText(f'Confirmation failed, try again!')
				self.messageBox.show()
		else:
			self.messageBox.setText(f'Wrong password!')
			self.messageBox.show()


	@QtCore.pyqtSlot(UserAccount)
	def enter(self, account : UserAccount):
		self._currentUser = account
		self.show()