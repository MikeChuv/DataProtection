# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mchuv\Docs\DataProtection\Lab06\src\ui\regPartitionEnterDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_regPartitionEnterDialog(object):
    def setupUi(self, regPartitionEnterDialog):
        regPartitionEnterDialog.setObjectName("regPartitionEnterDialog")
        regPartitionEnterDialog.resize(400, 300)
        font = QtGui.QFont()
        font.setPointSize(12)
        regPartitionEnterDialog.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(regPartitionEnterDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(regPartitionEnterDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.lineEdit = QtWidgets.QLineEdit(regPartitionEnterDialog)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 64, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.buttonBox = QtWidgets.QDialogButtonBox(regPartitionEnterDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(regPartitionEnterDialog)
        self.buttonBox.accepted.connect(regPartitionEnterDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(regPartitionEnterDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(regPartitionEnterDialog)

    def retranslateUi(self, regPartitionEnterDialog):
        _translate = QtCore.QCoreApplication.translate
        regPartitionEnterDialog.setWindowTitle(_translate("regPartitionEnterDialog", "Ввод имени раздела реестра"))
        self.label.setText(_translate("regPartitionEnterDialog", "Имя раздела реестра:"))