
from Crypto.Hash import MD4
from PyQt5 import QtWidgets, QtCore

from ui.ui_decryptUsersDialog import Ui_decryptUsersDialog

class DecryptUsersDialog(QtWidgets.QDialog):

	onPasswordEntered = QtCore.pyqtSignal(bytes)

	def __init__(self, parent=None):
		super(DecryptUsersDialog, self).__init__(parent)

		self.ui = Ui_decryptUsersDialog()
		self.ui.setupUi(self)

		self.ui.buttonBox.accepted.connect(self.entered)


	def entered(self):
		text = self.ui.passEdit.text()
		hashObject = MD4.new(text.encode('utf-8'))
		self.onPasswordEntered.emit(hashObject.digest())
		del text
		del hashObject
