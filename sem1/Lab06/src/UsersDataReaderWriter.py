import json
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from typing import List

from UserAccount import UserAccount

class UsersDataReaderWriter(object):

	def __init__(self, filename : str, k : bytes):
		self._fileName = filename
		self.cipher = AES.new(k, AES.MODE_ECB)

	def __enter__(self):
		try:
			self._file = open(self._fileName, 'rb+')
		except FileNotFoundError:
			self._file = open(self._fileName, 'wb+')
			defaultAdmin = {'login' : 'ADMIN', 'password' : '', 'blocked' : 0, 'restrictions' : 0}
			data = json.dumps(defaultAdmin).encode(encoding='UTF-8')
			data = self.cipher.encrypt(pad(data, 16))
			self._file.write(data)
			self._file.seek(0)
		return self


	def __exit__(self, exc_type, exc_val, exc_tb):
		self._file.close()


	def readData(self) -> list:
		assert self._file.closed == False
		data = self._file.read()
		data = self.cipher.decrypt(data)
		try:
			data = unpad(data, 16)
			data = data.decode(encoding='UTF-8')
			self._userList = json.loads(data)
			if type(self._userList) == dict:
				self._userList = [self._userList]
			return self._userList
		except ValueError as e:
			raise ValueError('Неверный пароль')


		

	def writeData(self, data : List[UserAccount]) -> None:
		assert self._file.closed == False
		dictData : List[dict] = [x.asDict() for x in data]
		jsonData = json.dumps(dictData).encode(encoding='UTF-8')
		data = self.cipher.encrypt(pad(jsonData, 16))
		self._file.write(data)
