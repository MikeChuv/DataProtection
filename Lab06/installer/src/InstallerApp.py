import os
import PyInstaller.__main__
from PyQt5 import QtCore, QtWidgets

from SearchFolderDialog import SearchFolderDialog


class InstallerApp(QtWidgets.QApplication):
	
	def __init__(self):
		super().__init__([])
		self.searchFolderDialog = SearchFolderDialog()
		sourceDir = os.path.abspath(os.path.join(os.path.abspath(__file__), *([os.pardir]*3)))
		source = os.path.join(sourceDir, 'src/main.py')
		appName = 'Lab06'
		installerDir = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))
		splashScreen = os.path.join(installerDir, 'logo.png')
		# PyInstaller.__main__.run([
		#     f'--name={appName}',
		#     '--windowed',
		# 	'--noconfirm',
		#     source
		# ])
		self.searchFolderDialog.setAppName(appName)

	def start(self):
		self.searchFolderDialog.show()
		super().exec()