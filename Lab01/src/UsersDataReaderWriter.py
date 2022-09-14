
from UserAccount import UserAccount
import json
from typing import List

class UsersDataReaderWriter(object):

	def __init__(self, filename : str):
		self._fileName = filename

	def __enter__(self):
		try:
			self._file = open(self._fileName, 'r+')
		except FileNotFoundError:
			self._file = open(self._fileName, 'w+')
			defaultAdmin = {'login' : 'ADMIN', 'password' : '', 'blocked' : 0, 'restrictions' : 0}
			dat = json.dumps(defaultAdmin)
			self._file.write(dat)
			self._file.seek(0)
		
		return self


	def __exit__(self, exc_type, exc_val, exc_tb):
		self._file.close()


	def readData(self) -> list:
		assert self._file.closed == False
		# self._textData = self._file.readlines()
		# self._file.seek(0)
		# print(self._textData)
		self._userList = json.load(self._file)
		if type(self._userList) == dict:
			self._userList = [self._userList]
		print(self._userList)
		return self._userList


		

	def writeData(self, data : List[UserAccount]):
		assert self._file.closed == False
		dictData : List[dict] = [x.asDict() for x in data]
		jsonData = json.dumps(dictData)
		self._file.write(jsonData)
