import os
import win32api
import psutil
import winreg
from Crypto.Hash import SHA
from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from PyQt5 import QtWidgets, QtCore

from ui.ui_regPartitionEnterDialog import Ui_regPartitionEnterDialog

class RegPartitionEnterDialog(QtWidgets.QDialog):

	onKeyChecked = QtCore.pyqtSignal()

	sourceDir = os.path.abspath(__file__)

	def __init__(self, parent=None):
		super(RegPartitionEnterDialog, self).__init__(parent)

		self.ui = Ui_regPartitionEnterDialog()
		self.ui.setupUi(self)

		self.messageBox = QtWidgets.QMessageBox(self)
		self.ui.buttonBox.accepted.connect(self.entered)

		self.accessRegistry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)


	def entered(self):
		text = self.ui.lineEdit.text().strip()
		try:
			accessKey = winreg.OpenKey(self.accessRegistry, fr"SOFTWARE\{text}")
		except FileNotFoundError:
			self.messageBox.setWindowTitle('Error')
			self.messageBox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
			self.messageBox.setText(f'No key for "{text}"')
			self.messageBox.exec_()
			self.close()
			return
		value, t = winreg.QueryValueEx(accessKey, 'Signature')
		info = self.getPCInfo()
		myhash = SHA.new(info.encode('utf8'))
		keyPath = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))
		keyPath = os.path.join(keyPath, 'rsa_key.bin')
		publickey = RSA.importKey(open(keyPath).read())
		if publickey is not None:
			try:
				pkcs1_15.new(publickey).verify(myhash, value)
				self.onKeyChecked.emit()
			except ValueError:
				self.messageBox.setWindowTitle('Error')
				self.messageBox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
				self.messageBox.setText(f'Signature check fail!')
				self.messageBox.exec_()
				self.close()
				return


	def getPCInfo(self):
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