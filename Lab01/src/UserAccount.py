

class UserAccount:

	_login : str = ''
	_password : str = ''

	_blocked : int = 0
	_hasPasswordRestriction : int = 0

	m = 1114112 # alphabet size

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


	##################################
	#### Encryption
	##################################

	def _encryptBlock(self, block, key):
		# cut key to block size
		k = key[:len(block)]
		c = ''
		for pi, ki in zip(block, k):
			c += chr((ord(pi) + ord(ki)) % self.m)
		return c

	def _decryptBlock(self, block, key):
		k = key[:len(block)]
		phrase = ''
		for ci, ki in zip(block, k):
			phrase += chr((ord(ci) + self.m - ord(ki)) % self.m)
		return phrase


	def encrypt(self, phrase : str, key : str) -> str:
		if len(key) == 0:
			return ''
		elif len(phrase) > len(key):
			l = len(key)
			blocks = list(phrase[0+i:l+i] for i in range(0, len(phrase), l))
			res = ''
			for block in blocks:
				cipher = self._encryptBlock(block, key)
				res += cipher
			return res
		elif len(phrase) <= len(key):
			cipher = self._encryptBlock(phrase, key)
			return cipher


	def decrypt(self, cipher, key):
		if len(key) == 0:
			return ''
		elif len(cipher) > len(key):
			l = len(key)
			blocks = list(cipher[0+i:l+i] for i in range(0, len(cipher), l))
			res = ''
			for block in blocks:
				origPhrase = self._decryptBlock(block, key)
				res += origPhrase
			return res			
		elif len(cipher) <= len(key):
			origPhrase = self._decryptBlock(cipher, key)
			return origPhrase


	#####################################
	
	def hasAuthData(self, login : str, password : str) -> bool:
		if self._login == login and self._password == self.encrypt(login, password[::-1]):
		# if self._login == login == self.decrypt(self._password, password):
			return True
		else: return False
		


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
		self._password = self.encrypt(self._login, password[::-1])



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


	