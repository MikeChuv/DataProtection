# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v:\Dev\DataProtection\sem2\Lab01\src\ui\authDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AuthDialog(object):
    def setupUi(self, AuthDialog):
        AuthDialog.setObjectName("AuthDialog")
        AuthDialog.resize(459, 306)
        font = QtGui.QFont()
        font.setPointSize(12)
        AuthDialog.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(AuthDialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(AuthDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(AuthDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.userNameLabel = QtWidgets.QLabel(AuthDialog)
        self.userNameLabel.setText("")
        self.userNameLabel.setObjectName("userNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.userNameLabel)
        self.passwordLabel = QtWidgets.QLabel(AuthDialog)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.passwordEdit = QtWidgets.QLineEdit(AuthDialog)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordEdit)
        self.gridLayout.addLayout(self.formLayout, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)

        self.retranslateUi(AuthDialog)
        self.buttonBox.accepted.connect(AuthDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(AuthDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(AuthDialog)

    def retranslateUi(self, AuthDialog):
        _translate = QtCore.QCoreApplication.translate
        AuthDialog.setWindowTitle(_translate("AuthDialog", "Аутентификация"))
        self.label_2.setText(_translate("AuthDialog", "Имя пользователя:"))
        self.passwordLabel.setText(_translate("AuthDialog", "Пароль:"))
