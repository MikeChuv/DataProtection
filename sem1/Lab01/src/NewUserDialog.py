
from PyQt5 import QtWidgets

from forms.newUserDialogWindow import Ui_newUserDialog

class NewUserDialog(QtWidgets.QDialog):
	def __init__(self, parent):
		super(NewUserDialog, self).__init__(parent)

		self.ui = Ui_newUserDialog()
		self.ui.setupUi(self)