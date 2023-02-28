import shutil
import os
import ctypes
import win32api
import psutil
import winreg
import PyInstaller.__main__
from PyQt5 import QtWidgets, QtCore, QtGui

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA


from ui.ui_searchFolder import Ui_selectFolderDialog

class SearchFolderDialog(QtWidgets.QDialog):

	sourceDir = os.path.abspath(os.path.join(os.path.abspath(__file__), *([os.pardir]*3)))
	sourceDir = os.path.join(sourceDir, 'dist')

	def __init__(self, parent=None):
		super().__init__(parent)

		self.ui = Ui_selectFolderDialog()
		self.ui.setupUi(self)

		self.ui.searchFolderButton.clicked.connect(self.search)
		self.ui.buttonBox.accepted.connect(self.processPath)
		self.ui.buttonBox.accepted.disconnect(self.accept)
		self.ui.buttonBox.rejected.connect(self.rejectedCallback)

		self.messageBox = QtWidgets.QMessageBox(self)

		self.accessRegistry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
		self.wantToClose = False

	def setAppName(self, name : str):
		self.appName = name

	@QtCore.pyqtSlot()
	def search(self):
		self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
		self.folderpath = os.path.abspath(self.folderpath)
		self.ui.destDirLabel.setText(self.folderpath)

	def rejectedCallback(self):
		self.wantToClose = True
		self.close()


	def processPath(self):
		try:
			self.ui.buttonBox.buttons()[0].setEnabled(False)
			self.setWindowTitle('Installing...')
			try:
				# if os.path.exists(self.folderpath):
				# 	shutil.rmtree(self.folderpath)
				shutil.copytree(self.sourceDir, self.folderpath, dirs_exist_ok=True)
			except OSError as e:
				self.messageBox.setWindowTitle('Error')
				self.messageBox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
				self.messageBox.setText(f'Directory not copied. Error: {e}')
				self.messageBox.setModal(True)
				# self.messageBox.show()
				self.messageBox.exec_()
			
			text = self.getPCInfo()
			keys = RSA.generate(1024)

			# privatekey = keys.exportKey(format='PEM', passphrase=None, pkcs=1, protection=None, randfunc=None) 

			publickey = keys.publickey().exportKey('PEM') 
			keyPath = os.path.join(self.folderpath, self.appName)
			keyPath = os.path.join(keyPath, 'rsa_key.bin')
			# print(keyPath)
			with open(keyPath, 'wb') as out:
				out.write(publickey)
			myhash = SHA.new(text.encode('utf8'))
			signature = pkcs1_15.new(keys)
			sig = signature.sign(myhash)

			regKey = self.ui.regPartLineEdit.text().strip()
			if regKey == '':
				raise ValueError('Reg key is not set!')
			accessKey = winreg.CreateKeyEx(self.accessRegistry, fr"SOFTWARE\{regKey}")
			winreg.SetValueEx(accessKey, "Signature", 0, winreg.REG_BINARY, sig)

			# print(myhash.hexdigest())
			self.messageBox.setWindowTitle('Ok')
			self.messageBox.setIcon(QtWidgets.QMessageBox.Icon.Information)
			self.messageBox.setText('Installed')
			self.messageBox.setModal(True)
			# self.messageBox.show()
			self.messageBox.exec_()
			self.wantToClose = True
			self.close()
		except Exception as e:
			self.messageBox.setWindowTitle('Error')
			self.messageBox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
			self.messageBox.setText(f'Error: {e}')
			self.messageBox.setModal(True)
			# self.messageBox.show()
			self.messageBox.exec_()
			self.ui.buttonBox.buttons()[0].setEnabled(False)


	def getPCInfo(self) -> str:
		text = os.getlogin()
		text += os.environ['COMPUTERNAME']
		text += os.environ['SYSTEMROOT']
		text += str(win32api.GetSystemMetrics(43)) # mouse buttons
		text += str(win32api.GetSystemMetrics(1)) # screen height
		drive, _ = os.path.splitdrive(self.sourceDir)
		partitions = psutil.disk_partitions()
		drives = ''
		fstype = None
		for p in partitions:
			drives += p.device
			if p.device == f'{drive}\\':
				fstype = p.fstype
		text += drives
		text += str(psutil.virtual_memory().total) # ram volume
		text += fstype
		return text




	def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
		if self.wantToClose:
			return super().closeEvent(a0)
		else:
			# self.show()
			a0.ignore()
