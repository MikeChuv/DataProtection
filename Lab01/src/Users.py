
from typing import Union, List


from Admin import Admin
from UserAccount import UserAccount
from UsersDataReaderWriter import UsersDataReaderWriter




class Users:

	_userList : List[UserAccount] = []
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
						user['blocked'], \
						user['restrictions']
					)
				else:
					acc = UserAccount(
						user['login'], \
						user['password'], \
						user['blocked'], \
						user['restrictions']
					)
				
				self._userList.append(acc)


	def __getitem__(self, i : int) -> UserAccount:
		return self._userList[i]

	def __setitem__(self, i : int, item : UserAccount):
		self._userList[i] = item

	def __len__(self):
		return len(self._userList)

	def getAccount(self, login : str, password : str) -> Union[UserAccount, None]:
		for user in self._userList:
			if user.hasAuthData(login, password):
				return user
		return None


	def hasAccountWithLogin(self, login : str) -> bool:
		for user in self._userList:
			if user.login.lower() == login.lower():
				return True
		return False


	def updateAccount(self, old : UserAccount, new : UserAccount) -> None:
		for i in range(len(self._userList)):
			if self._userList[i] == old:
				self._userList[i] = new

	def addAccount(self, acc : UserAccount):
		self._userList.append(acc)

	def addAccountByLogin(self, login : str):
		acc = UserAccount(login, '', 0, 0)
		self._userList.append(acc)

	def save(self):
		with UsersDataReaderWriter(self._accountsFileName) as writer:
			writer.writeData(self._userList)
