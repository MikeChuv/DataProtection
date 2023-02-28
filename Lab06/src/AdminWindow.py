
from PyQt5 import QtWidgets, QtCore

from AboutDialog import AboutDialog
from Admin import Admin
from ChangePasswordDialog import ChangePasswordDialog
from Users import Users

from ui.ui_admin import Ui_AdminWindow

class AdminWindow(QtWidgets.QMainWindow):
	
	onExit = QtCore.pyqtSignal(Users)

	def __init__(self, parent):
		super(AdminWindow, self).__init__(parent)

		self.ui = Ui_AdminWindow()
		self.ui.setupUi(self)

		self.aboutDialog : QtWidgets.QDialog = AboutDialog(self)
		self.changePasswordDialog = ChangePasswordDialog(self)
		self.messageBox = QtWidgets.QMessageBox(self)

		self.ui.actionAbout.triggered.connect(self.aboutDialog.show)
		self.ui.actionExit.triggered.connect(self.closeAdmin)
		self.ui.actionChange_password.triggered.connect(self.changePassword)
		self.ui.addNewUserButton.clicked.connect(self.addNewUser)

		self.ui.usersTableWidget.itemChanged.connect(self.tableInput)

		self.changePasswordDialog.onPasswordChanged.connect(self.setAdmin)


	@QtCore.pyqtSlot(QtWidgets.QTableWidgetItem)
	def tableInput(self, item : QtWidgets.QTableWidgetItem):
		row = item.row()
		col = item.column()
		if col == 1: self._users[row].blocked = item.checkState()
		if col == 2: self._users[row].hasPasswordRestriction = item.checkState()


	@QtCore.pyqtSlot(Admin, Users)
	def enter(self, admin : Admin, users : Users):
		self._currentAdmin : Admin = admin
		self._users : Users = users
		self.updateTable()
		self.show()



	@QtCore.pyqtSlot(Admin)
	def setAdmin(self, admin : Admin):
		if isinstance(admin, Admin):
			self._users.updateAccount(self._currentAdmin, admin)
			self._currentAdmin = admin
		else: raise 'This user is not an admin'
		

	def closeAdmin(self):
		if self.aboutDialog.isVisible(): self.aboutDialog.close()
		self.onExit.emit(self._users)
		self.close()

	def changePassword(self):
		self.changePasswordDialog.enter(self._currentAdmin)


	def addNewUser(self):
		login = self.ui.newUserLoginEdit.text()
		if self._users.hasAccountWithLogin(login):
			self.messageBox.setText(f'Login [{login}] is already used, make a new one!')
			self.messageBox.show()
		else:
			self._users.addAccountByLogin(login)
			self.updateTable()
		self.ui.newUserLoginEdit.clear()


	def updateTable(self):
		self.ui.usersTableWidget.setRowCount(len(self._users))
		for i, u in enumerate(self._users):
			loginItem = QtWidgets.QTableWidgetItem(u.login)
			self.ui.usersTableWidget.setItem(i, 0, loginItem)
			blockedItem = QtWidgets.QTableWidgetItem()
			blockedItem.setCheckState(u.blocked)
			self.ui.usersTableWidget.setItem(i, 1, blockedItem)
			if isinstance(u, Admin): 
				flags = blockedItem.flags()
				blockedItem.setFlags(flags & ~32)
			hasRestrictionItem = QtWidgets.QTableWidgetItem()
			hasRestrictionItem.setCheckState(u.hasPasswordRestriction)
			self.ui.usersTableWidget.setItem(i, 2, hasRestrictionItem)
		


	
