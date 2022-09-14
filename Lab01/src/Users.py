
from UserAccount import UserAccount
from Admin import Admin
from UsersDataReaderWriter import UsersDataReaderWriter


from typing import Union, List


class Users:

	_userList = []
	_accountsFileName = ''

	def __init__(self, accountsFileName : str):
		self._accountsFileName = accountsFileName
		with UsersDataReaderWriter(self._accountsFileName) as reader:
			userDictList = reader.readData()
			for user in userDictList:
				if user['login'] == 'ADMIN':
					acc = Admin(
						user['login'], \
						user['password'], \
						bool(user['blocked']), \
						bool(user['restrictions'])
					)
				else:
					acc = UserAccount(
						user['login'], \
						user['password'], \
						bool(user['blocked']), \
						bool(user['restrictions'])
					)
				
				self._userList.append(acc)


	def getAccount(self, login : str, password : str) -> Union[UserAccount, None]:
		flag = False
		for user in self._userList:
			if user.login == login and user.password == password:
				flag = True
				return user

		if not flag: return None


	def save(self):
		with UsersDataReaderWriter(self._accountsFileName) as writer:
			writer.writeData(self._userList)
