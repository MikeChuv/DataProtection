
from PyQt5 import QtWidgets

from ui.ui_about import Ui_aboutDialog

class AboutDialog(QtWidgets.QDialog):
	def __init__(self, parent):
		super(AboutDialog, self).__init__(parent)

		self.ui = Ui_aboutDialog()
		self.ui.setupUi(self)