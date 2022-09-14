


from typing import overload


class UserAccount:

	_login : str = ''
	_password : str = ''

	_blocked : bool = False
	_hasPasswordRestriction : bool = False


	def __init__(self):
		pass


	def __init__(self, login : str, password : str, blocked : bool, restrictions : bool):
		self._login = login
		self._password = password
		self._blocked = blocked
		self._hasPasswordRestriction = restrictions


	def __repr__(self):
		return f"login: {self.login}, \t password: {self.password}"

	def isAdmin(self):
		return False

	def asDict(self):
		accDict = {
			'login' : self._login,
			'password' : self._password,
			'blocked' : int(self._blocked),
			'restrictions' : int(self._hasPasswordRestriction)
		}
		return accDict

	@property
	def login(self):
		return self._login

	#####################################
	
	@property
	def password(self):
		return self._password


	@password.setter
	def password(self, password : str):
		self._password = password



	##################################

	@property
	def blocked(self):
		return self._blocked

	@blocked.setter
	def blocked(self, blocked : bool):
		self._blocked = blocked


	###################################

	@property
	def hasPasswordRestriction(self):
		return self._hasPasswordRestriction

	@hasPasswordRestriction.setter
	def hasPasswordRestriction(self, restriction : bool):
		self._hasPasswordRestriction = restriction


	