# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v:\Dev\DataProtection\sem2\Lab01\ui\newUserDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_newUserDialog(object):
    def setupUi(self, newUserDialog):
        newUserDialog.setObjectName("newUserDialog")
        newUserDialog.setWindowModality(QtCore.Qt.WindowModal)
        newUserDialog.resize(432, 301)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(newUserDialog.sizePolicy().hasHeightForWidth())
        newUserDialog.setSizePolicy(sizePolicy)
        newUserDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(newUserDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(newUserDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 78, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.newUserLoginLabel = QtWidgets.QLabel(newUserDialog)
        self.newUserLoginLabel.setObjectName("newUserLoginLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.newUserLoginLabel)
        self.newUserLoginEdit = QtWidgets.QLineEdit(newUserDialog)
        self.newUserLoginEdit.setObjectName("newUserLoginEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.newUserLoginEdit)
        self.newPasswordLabel = QtWidgets.QLabel(newUserDialog)
        self.newPasswordLabel.setObjectName("newPasswordLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.newPasswordLabel)
        self.newPasswordEdit = QtWidgets.QLineEdit(newUserDialog)
        self.newPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPasswordEdit.setObjectName("newPasswordEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.newPasswordEdit)
        self.confirmNewPasswordLabel = QtWidgets.QLabel(newUserDialog)
        self.confirmNewPasswordLabel.setObjectName("confirmNewPasswordLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.confirmNewPasswordLabel)
        self.confirmNewPasswordEdit = QtWidgets.QLineEdit(newUserDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirmNewPasswordEdit.sizePolicy().hasHeightForWidth())
        self.confirmNewPasswordEdit.setSizePolicy(sizePolicy)
        self.confirmNewPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmNewPasswordEdit.setObjectName("confirmNewPasswordEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.confirmNewPasswordEdit)
        self.gridLayout.addLayout(self.formLayout, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem3, 4, 1, 1, 1)

        self.retranslateUi(newUserDialog)
        self.buttonBox.accepted.connect(newUserDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(newUserDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(newUserDialog)

    def retranslateUi(self, newUserDialog):
        _translate = QtCore.QCoreApplication.translate
        newUserDialog.setWindowTitle(_translate("newUserDialog", "New User"))
        self.newUserLoginLabel.setText(_translate("newUserDialog", "Имя пользователя"))
        self.newPasswordLabel.setText(_translate("newUserDialog", "Пароль"))
        self.confirmNewPasswordLabel.setText(_translate("newUserDialog", "Подтвердите пароль"))
