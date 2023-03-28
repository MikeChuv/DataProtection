
from PyQt5 import QtWidgets, QtCore, QtGui
import os

from NewUserDialog import NewUserDialog
from AboutDialog import AboutDialog
from AuthDialog import AuthDialog
from Document import Document
from User import User, Users
from PublicKey import PublicKey


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
        self.ui.actionPickSK.triggered.connect(self.__startChangeUser)
        self.ui.btnPickUser.clicked.connect(self.__startChangeUser)
        self.ui.actionPKImport.triggered.connect(self.__importPublicKey)
        self.ui.actionPKExport.triggered.connect(self.__exportPublicKey)
        self.ui.actionDelKeysPair.triggered.connect(self.__delKeyPair)
        self.ui.userNameEdit.returnPressed.connect(self.__changeUser)
        self.__setUiEnabled(False)
        self.users = Users.load(self.usersPath)
        self.currentUser = None
        self.currentDocument = None

    def __setUiEnabled(self, enabled : bool):
        self.ui.actionLoad.setEnabled(enabled)
        self.ui.actionCreate.setEnabled(enabled)
        self.ui.actionSave.setEnabled(enabled)
        self.ui.btnSaveDoc.setEnabled(enabled)
        self.ui.actionPKImport.setEnabled(enabled)
        self.ui.actionPKExport.setEnabled(enabled)
        self.ui.actionDelKeysPair.setEnabled(enabled)

        self.ui.btnLoadDoc.setEnabled(enabled)
        self.ui.btnSaveDoc.setEnabled(enabled)
        self.ui.userNameEdit.setEnabled(enabled)
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
            messageBox = QtWidgets.QMessageBox(self)
            messageBox.setText(f'Документ будет закрыт, возможна потеря данных')
            messageBox.exec()
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
        pkPath = os.path.join(self.parDir, 'PK', self.currentUser.name, document.userName)
        if not os.path.exists(pkPath):
            messageBox = QtWidgets.QMessageBox(self)
            messageBox.setText(f'Не проимпортирован ключ для автора {document.userName}')
            messageBox.exec()
            return 
        pk = None
        with open(pkPath, 'rb') as r:
            pk = PublicKey.unpack(r)
        if pk and pk.isSignatureValid(self.currentUser.keys.public_key()):
            self.currentDocument = document
            self.ui.textEdit.setText(self.currentDocument.text)
            self.setWindowTitle(f'Подписанный документ {loadDocFileName.split(os.sep)[-1]} от {document.userName}')
        else:
            messageBox = QtWidgets.QMessageBox(self)
            messageBox.setText(f'Проверка подписи не пройдена')
            messageBox.exec()
            return



    @QtCore.pyqtSlot()
    def __saveDocument(self):
        if not self.currentUser or self.currentUser.state != User.AccessState.ALLOWED:
            messageBox = QtWidgets.QMessageBox(self)
            messageBox.setText(f'Документ не сохранен, так как пользователь не задан или не прошел аутентификацию')
            messageBox.exec()
            return
        # doc = self.ui.textEdit.document()
        text = self.ui.textEdit.toPlainText()
        try:
            self.currentDocument = Document.fromPlainText(text, self.currentUser)
            saveFileName, filter = QtWidgets.QFileDialog.getSaveFileName(
                self, 
                "Выбор файла для сохранения документа",
                filter='*.sd'
            )
            if not saveFileName:
                return
            with open(saveFileName, 'wb') as w:
                self.currentDocument.pack(w)
                self.setWindowTitle(f'Подписанный документ {saveFileName.split(os.sep)[-1]} от {self.currentDocument.userName}')
        except ValueError as e:
            messageBox = QtWidgets.QMessageBox(self)
            messageBox.setText(f'Документ не сохранен, так как пользователь не прошел аутентификацию')
            messageBox.exec()


    @QtCore.pyqtSlot()
    def __startChangeUser(self):
        self.ui.userNameEdit.clear()
        if self.currentDocument and \
            self.currentDocument.text != self.ui.textEdit.toPlainText():
            messageBox = QtWidgets.QMessageBox(self)
            messageBox.setText(f'Документ будет закрыт, возможна потеря данных')
            messageBox.exec()
        if self.currentUser:
            self.currentUser.exit()
        self.ui.textEdit.clear()
        self.currentDocument = None
        self.setWindowTitle('Документооборот')
        self.__setUiEnabled(False)
        self.ui.userNameEdit.setEnabled(True)
        self.ui.userNameEdit.setFocus()
        
    @QtCore.pyqtSlot()
    def __changeUser(self):
        userName = self.ui.userNameEdit.text().strip()
        if not userName:
            messageBox = QtWidgets.QMessageBox(self)
            messageBox.setText(f'Имя пользователя не задано')
            messageBox.exec()
            return
        try:
            user = self.users[userName]
            passwd = AuthDialog.execute(self, userName)
            state = user.auth(passwd)
            if state == User.AccessState.ALLOWED:
                self.currentUser = user
                self.__setUiEnabled(True)
            else:
                messageBox = QtWidgets.QMessageBox(self)
                messageBox.setText(f'Неверный пароль')
                messageBox.exec()
        except KeyError as e:
            userData = NewUserDialog.execute(self, userName)
            if userData is not None:
                self.currentUser = User.create(
                    userData.userName, 
                    userData.passwd
                )
                self.users[userName] = self.currentUser
                self.__setUiEnabled(True)
            else:
                return
        self.ui.userNameEdit.setEnabled(False)

    @QtCore.pyqtSlot()
    def __importPublicKey(self):
        importFileName, filter = QtWidgets.QFileDialog.getOpenFileName(
            self, 
            "Выбор файла для импорта открытого ключа",
            filter='*.pub'
        )
        if not importFileName:
            return
        res = None
        with open(importFileName, 'rb') as infile:
            res = PublicKey.unpack(infile)
        res.makeSignature(self.currentUser.keys)
        newdata = res.packb(includeSignature=True)
        saveDir = os.path.join(self.parDir, 'PK', self.currentUser.name)
        if not os.path.exists(saveDir):
            os.mkdir(saveDir)
        savePath = os.path.join(self.parDir, 'PK', self.currentUser.name, res.ownerName)
        with open(savePath, 'wb') as outfile:
            outfile.write(newdata)
        # keypair = 
        # keys = RSA.import_key(keypair,passphrase=None)
        pass


    @QtCore.pyqtSlot()
    def __exportPublicKey(self):
        exportFolder = QtWidgets.QFileDialog.getExistingDirectory(self, "Выбор папки для экспорта открытого ключа")
        data = self.currentUser.exportPublicKey()
        filename = os.path.join(exportFolder, f'{self.currentUser.name}.pub')
        with open(filename, 'wb') as outfile:
            outfile.write(data)

    @QtCore.pyqtSlot()
    def __delKeyPair(self):
        if self.currentUser and self.currentUser.state == User.AccessState.ALLOWED:
            self.users.pop(self.currentUser.name)
            self.ui.textEdit.clear()
            self.currentDocument = None
            self.setWindowTitle('Документооборот')
            self.ui.userNameEdit.clear()


    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.users.save(self.usersPath)
        return super().closeEvent(a0)
    

