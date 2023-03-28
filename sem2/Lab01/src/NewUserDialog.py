import typing
from PyQt5 import QtWidgets, QtCore, QtGui

from ui.ui_newUserDialog import Ui_newUserDialog

class NewUserDialog(QtWidgets.QDialog):

    class UserData(typing.NamedTuple):
        userName : str
        passwd   : str

    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_newUserDialog()
        self.ui.setupUi(self)

    @staticmethod
    def execute(parent : QtWidgets.QWidget, userName : str) -> typing.Union[UserData, None]:
        dialog = NewUserDialog(parent)
        dialog.ui.newUserLoginEdit.setText(userName)
        dialog.exec()
        return dialog.getUserData()
    

    def getUserData(self) -> typing.Union[UserData, None]:
        name = self.ui.newUserLoginEdit.text()
        passwd = self.ui.newPasswordEdit.text()
        passwdConfirm = self.ui.confirmNewPasswordEdit.text()
        if name and passwd == passwdConfirm:
            self.ui.newUserLoginEdit.clear()
            self.ui.newPasswordEdit.clear()
            self.ui.confirmNewPasswordEdit.clear()
            return NewUserDialog.UserData(name, passwd)



    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        name = self.ui.newUserLoginEdit.text()
        passwd = self.ui.newPasswordEdit.text()
        passwdConfirm = self.ui.confirmNewPasswordEdit.text()
        if name and passwd == passwdConfirm:
            pass
        elif name:
            self.ui.newPasswordEdit.clear()
            self.ui.confirmNewPasswordEdit.clear()
            return a0.ignore()
        else:
            # ? put entered name?
            print('No user name')
            self.ui.newUserLoginEdit.clear()
            self.ui.newPasswordEdit.clear()
            self.ui.confirmNewPasswordEdit.clear()
        return super().closeEvent(a0)