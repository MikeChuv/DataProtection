# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mchuv\Docs\DataProtection\Lab06\ui\decryptUsersDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_decryptUsersDialog(object):
    def setupUi(self, decryptUsersDialog):
        decryptUsersDialog.setObjectName("decryptUsersDialog")
        decryptUsersDialog.resize(488, 188)
        font = QtGui.QFont()
        font.setPointSize(12)
        decryptUsersDialog.setFont(font)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(decryptUsersDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.promptLabel = QtWidgets.QLabel(decryptUsersDialog)
        self.promptLabel.setObjectName("promptLabel")
        self.verticalLayout.addWidget(self.promptLabel)
        self.passEdit = QtWidgets.QLineEdit(decryptUsersDialog)
        self.passEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passEdit.setObjectName("passEdit")
        self.verticalLayout.addWidget(self.passEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(decryptUsersDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(decryptUsersDialog)
        self.buttonBox.accepted.connect(decryptUsersDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(decryptUsersDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(decryptUsersDialog)

    def retranslateUi(self, decryptUsersDialog):
        _translate = QtCore.QCoreApplication.translate
        decryptUsersDialog.setWindowTitle(_translate("decryptUsersDialog", "Расшифрование файла учетных записей"))
        self.promptLabel.setText(_translate("decryptUsersDialog", "Парольная фраза для расшифрования"))
