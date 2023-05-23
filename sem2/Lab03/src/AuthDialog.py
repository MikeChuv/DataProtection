import typing
from PyQt5 import QtWidgets, QtCore, QtGui

from ui.ui_authDialog import Ui_AuthDialog

class AuthDialog(QtWidgets.QDialog):

    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_AuthDialog()
        self.ui.setupUi(self)
        self.userName = None

    @staticmethod
    def execute(parent : QtWidgets.QWidget) -> str:
        dialog = AuthDialog(parent)
        dialog.exec()
        return dialog.ui.passwordEdit.text()


    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        passwd = self.ui.passwordEdit.text()
        if not passwd:
            # TODO msgbox
            print('No passwd')
            self.ui.passwordEdit.clear()
        return super().closeEvent(a0)