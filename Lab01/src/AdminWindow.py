
from PyQt5 import QtWidgets, QtCore

from AboutDialog import AboutDialog
from Admin import Admin
from ChangePasswordDialog import ChangePasswordDialog

from forms.adminWindow import Ui_AdminWindow



class AdminWindow(QtWidgets.QMainWindow):
	def __init__(self, parent):
		super(AdminWindow, self).__init__(parent)

		self.ui = Ui_AdminWindow()
		self.ui.setupUi(self)

		self.aboutDialog : QtWidgets.QDialog = AboutDialog(self)
		self.changePasswordDialog = ChangePasswordDialog(self)

		self.ui.actionAbout.triggered.connect(self.aboutDialog.show)
		self.ui.actionExit.triggered.connect(self.closeAdmin)
		self.ui.actionChange_password.triggered.connect(self.changePassword)

		self.changePasswordDialog.onPasswordChanged.connect(self.setAdmin)


	@QtCore.pyqtSlot(Admin)
	def enter(self, admin : Admin):
		self._currentAdmin = admin
		self.show()

	@QtCore.pyqtSlot(Admin)
	def setAdmin(self, admin : Admin):
		if isinstance(admin, Admin):
			self._currentAdmin = admin
		else: raise 'This user is not an admin'
		

	def closeAdmin(self):
		if self.aboutDialog.isVisible(): self.aboutDialog.close()
		self.close()

	def changePassword(self):
		print('Admin change password')
		self.changePasswordDialog.enter(self._currentAdmin)

	
