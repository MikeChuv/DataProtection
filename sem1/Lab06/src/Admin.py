
from UserAccount import UserAccount

import typing

class Admin(UserAccount):


	def __init__(self, login : str, password : str, blocked : bool, restrictions : bool):
		super().__init__(login, password, blocked, restrictions)


	def isAdmin(self):
		return True

		