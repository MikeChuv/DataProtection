# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\passwordChangeDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangePasswordDialog(object):
    def setupUi(self, ChangePasswordDialog):
        ChangePasswordDialog.setObjectName("ChangePasswordDialog")
        ChangePasswordDialog.setWindowModality(QtCore.Qt.WindowModal)
        ChangePasswordDialog.resize(479, 206)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ChangePasswordDialog.sizePolicy().hasHeightForWidth())
        ChangePasswordDialog.setSizePolicy(sizePolicy)
        ChangePasswordDialog.setModal(True)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(ChangePasswordDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.oldPasswordLabel = QtWidgets.QLabel(ChangePasswordDialog)
        self.oldPasswordLabel.setObjectName("oldPasswordLabel")
        self.horizontalLayout.addWidget(self.oldPasswordLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.oldPasswordEdit = QtWidgets.QLineEdit(ChangePasswordDialog)
        self.oldPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.oldPasswordEdit.setObjectName("oldPasswordEdit")
        self.horizontalLayout.addWidget(self.oldPasswordEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.newPasswordLabel = QtWidgets.QLabel(ChangePasswordDialog)
        self.newPasswordLabel.setObjectName("newPasswordLabel")
        self.horizontalLayout_2.addWidget(self.newPasswordLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.newPasswordEdit = QtWidgets.QLineEdit(ChangePasswordDialog)
        self.newPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPasswordEdit.setObjectName("newPasswordEdit")
        self.horizontalLayout_2.addWidget(self.newPasswordEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.confirmNewPasswordLabel = QtWidgets.QLabel(ChangePasswordDialog)
        self.confirmNewPasswordLabel.setObjectName("confirmNewPasswordLabel")
        self.horizontalLayout_3.addWidget(self.confirmNewPasswordLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.confirmNewPasswordEdit = QtWidgets.QLineEdit(ChangePasswordDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirmNewPasswordEdit.sizePolicy().hasHeightForWidth())
        self.confirmNewPasswordEdit.setSizePolicy(sizePolicy)
        self.confirmNewPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmNewPasswordEdit.setObjectName("confirmNewPasswordEdit")
        self.horizontalLayout_3.addWidget(self.confirmNewPasswordEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(ChangePasswordDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(ChangePasswordDialog)
        self.buttonBox.accepted.connect(ChangePasswordDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(ChangePasswordDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ChangePasswordDialog)

    def retranslateUi(self, ChangePasswordDialog):
        _translate = QtCore.QCoreApplication.translate
        ChangePasswordDialog.setWindowTitle(_translate("ChangePasswordDialog", "Password change"))
        self.oldPasswordLabel.setText(_translate("ChangePasswordDialog", "Old password"))
        self.newPasswordLabel.setText(_translate("ChangePasswordDialog", "New password"))
        self.confirmNewPasswordLabel.setText(_translate("ChangePasswordDialog", "Confirm new password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChangePasswordDialog = QtWidgets.QDialog()
    ui = Ui_ChangePasswordDialog()
    ui.setupUi(ChangePasswordDialog)
    ChangePasswordDialog.show()
    sys.exit(app.exec_())
