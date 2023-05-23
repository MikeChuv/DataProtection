
from PyQt5 import QtWidgets, QtCore, QtGui
import os
import OpenSSL.crypto
from ctypes import *

from AboutDialog import AboutDialog
from AuthDialog import AuthDialog
from Document import Document


from ui.ui_MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.curDir = os.path.dirname(os.path.abspath(__file__))
        self.parDir = os.path.dirname(self.curDir)
        self.usersPath = os.path.join(self.parDir, 'users.dat')

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.aboutDialog = AboutDialog(self)
        self.ui.actionAbout.triggered.connect(self.aboutDialog.show)
        self.ui.actionClose.triggered.connect(self.close)
        self.ui.actionLoad.triggered.connect(self.__loadDocument)
        self.ui.btnLoadDoc.clicked.connect(self.ui.actionLoad.trigger)
        self.ui.actionCreate.triggered.connect(self.__createNewDocument)
        self.ui.actionSave.triggered.connect(self.__saveDocument)
        self.ui.btnSaveDoc.clicked.connect(self.ui.actionSave.trigger)
        self.ui.actionPickCert.triggered.connect(self.__startChangeUser)
        self.ui.btnPickCert.clicked.connect(self.__startChangeUser)
        self.ui.actionDelCert.triggered.connect(self.__delCert)
        self.__setUiEnabled(False)
        self.currentUser = None
        self.currentPKCS12 = None
        self.currentDocument = None

    def __setUiEnabled(self, enabled : bool):
        self.ui.actionLoad.setEnabled(enabled)
        self.ui.actionCreate.setEnabled(enabled)
        self.ui.actionSave.setEnabled(enabled)
        self.ui.btnSaveDoc.setEnabled(enabled)
        self.ui.actionPKImport.setEnabled(enabled)
        self.ui.actionPKExport.setEnabled(enabled)
        self.ui.actionDelCert.setEnabled(enabled)

        self.ui.btnLoadDoc.setEnabled(enabled)
        self.ui.btnSaveDoc.setEnabled(enabled)
        self.ui.textEdit.setEnabled(enabled)


    @QtCore.pyqtSlot()
    def __createNewDocument(self):
        if self.currentDocument and \
            self.currentDocument.text != self.ui.textEdit.toPlainText():
            messageBox = QtWidgets.QMessageBox(self)
            messageBox.setText(f'Документ будет закрыт, возможна потеря данных')
            messageBox.exec()
        self.ui.textEdit.clear()
        self.setWindowTitle('Подписанный документ')

    @QtCore.pyqtSlot()
    def __loadDocument(self):
        if self.currentDocument and \
            self.currentDocument.text != self.ui.textEdit.toPlainText():
            self.__showMsgBox(f'Документ будет закрыт, возможна потеря данных')
        self.ui.textEdit.clear() 
        self.currentDocument = None
        self.setWindowTitle('Документооборот')
        loadDocFileName, filter = QtWidgets.QFileDialog.getOpenFileName(
            self, 
            "Выбор файла для загрузки документа",
            filter='*.sd'
        )
        if not loadDocFileName:
            return
        document = None
        with open(loadDocFileName, 'rb') as r:
            document = Document.unpack(r)

        if not document.verify():
            self.__showMsgBox(f'Проверка подписи не пройдена')
        else:
            self.currentDocument = document
            self.ui.textEdit.setText(self.currentDocument.text)
            self.setWindowTitle(f'Подписанный документ {os.path.basename(loadDocFileName)} от {document.cert.get_subject().CN}')



    @QtCore.pyqtSlot()
    def __saveDocument(self):
        if not self.currentPKCS12:
            self.__showMsgBox(f'Документ не сохранен, так как пользователь не задан или не прошел аутентификацию')
            return
        # doc = self.ui.textEdit.document()
        text = self.ui.textEdit.toPlainText()
        try:
            self.currentDocument = Document.fromPlainText(text, self.currentPKCS12)
            saveFileName, filter = QtWidgets.QFileDialog.getSaveFileName(
                self, 
                "Выбор файла для сохранения документа",
                filter='*.sd'
            )
            if not saveFileName:
                return
            with open(saveFileName, 'wb') as w:
                self.currentDocument.pack(w)
                self.setWindowTitle(f'Подписанный документ {os.path.basename(saveFileName)} от {self.currentDocument.cert.get_subject().CN}')
        except Exception as e:
            self.__showMsgBox(f'Документ не сохранен {e}')


    @QtCore.pyqtSlot()
    def __startChangeUser(self):
        self.ui.userNameEdit.clear()
        if self.currentDocument and \
            self.currentDocument.text != self.ui.textEdit.toPlainText():
            self.__showMsgBox(f'Документ будет закрыт, возможна потеря данных')

        if self.currentPKCS12:
            self.currentPKCS12 = None
            self.importedFilePath = None
        self.ui.textEdit.clear()
        self.currentDocument = None
        self.setWindowTitle('Документооборот')
        self.__setUiEnabled(False)
        self.__changeUser()

    def __showMsgBox(self, message : str):
        messageBox = QtWidgets.QMessageBox(self)
        messageBox.setText(message)
        messageBox.exec()
        
    @QtCore.pyqtSlot()
    def __changeUser(self):
        # open cert
        importFileName, filter = QtWidgets.QFileDialog.getOpenFileName(
            self, 
            "Выбор файла для импорта сертификата",
            filter='*.pfx'
        )
        if not importFileName:
            return
        passwd = AuthDialog.execute(self)

        with open(importFileName, 'rb') as inFile:
            pfx = inFile.read()
            try:
                self.currentPKCS12 = OpenSSL.crypto.load_pkcs12(pfx, passwd)
                self.importedFilePath = importFileName
                cert = self.currentPKCS12.get_certificate() 
                userName = cert.get_subject().CN
                self.ui.userNameEdit.setText(userName)
                self.__setUiEnabled(True)
            except OpenSSL.crypto.Error as e:
                self.__showMsgBox(f'Неверный пароль')

    @QtCore.pyqtSlot()
    def __delCert(self):
        if self.currentPKCS12:
            self.ui.textEdit.clear()
            self.currentDocument = None
            self.currentPKCS12 = None
            self.setWindowTitle('Документооборот')
            self.ui.userNameEdit.clear()
            os.remove(self.importedFilePath)


    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        return super().closeEvent(a0)
    

