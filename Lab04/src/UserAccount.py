

class UserAccount:

	_login : str = ''
	_password : str = ''

	_blocked : int = 0
	_hasPasswordRestriction : int = 0


	def __init__(self, login : str, password : str, blocked, restrictions):
		self._login = login
		self._password = password
		self._blocked = blocked
		self._hasPasswordRestriction = restrictions

	def __repr__(self):
		return f"login: {self.login}, password: {self.password}, blocked: {self.blocked}"



	def isAdmin(self):
		return False

	def asDict(self):
		accDict = {
			'login' : self._login,
			'password' : self._password,
			'blocked' : self._blocked,
			'restrictions' : self._hasPasswordRestriction
		}
		return accDict

	#####################################

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
	def blocked(self, blocked):
		self._blocked = blocked


	###################################

	@property
	def hasPasswordRestriction(self):
		return self._hasPasswordRestriction

	@hasPasswordRestriction.setter
	def hasPasswordRestriction(self, restriction):
		self._hasPasswordRestriction = restriction


	