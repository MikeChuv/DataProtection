
import typing
from enum import IntEnum
from PyQt5 import QtCore
from Crypto.PublicKey import RSA
import msgpack
import os
from PublicKey import PublicKey
from Singleton import Singleton




class User(QtCore.QObject):

    class AccessState(IntEnum):
        INIT    = 0
        ALLOWED = 1
        DENIED  = 2

    def __init__(self, userName : str, keyPair : bytes) -> None:
        assert len(userName) < 2 ** 16
        self.state = User.AccessState.INIT
        # TODO search for user
        # if found return reference, else create a new one
        self.name = userName
        self.importedKey = keyPair
        self.keys = None

    def auth(self, passwd : str) -> AccessState:
        assert self.state != User.AccessState.ALLOWED
        try:
            self.keys = RSA.import_key(self.importedKey, passphrase=passwd)
            self.pub = PublicKey(
                self.name,
                self.keys.public_key().export_key('PEM'),
            )
            self.state = User.AccessState.ALLOWED
            return self.state
        except Exception as e:
            self.state = User.AccessState.DENIED
            return self.state

    def exit(self):
        if self.state != User.AccessState.ALLOWED:
            return
        self.state = User.AccessState.INIT
        self.keys = None

    @classmethod
    def unpack(cls, data : dict):
        assert 'userName' in data
        assert 'keyPair' in data
        return cls(data['userName'], data['keyPair'])

    @classmethod
    def create(cls, userName : str, passwd : str):
        keys = RSA.generate(2048)
        user = cls(
            userName,
            keys.export_key(
                format='PEM',
                passphrase=passwd,
                pkcs=1,
                protection=None,
                randfunc=None
            )
        )
        user.state = user.auth(passwd)
        return user

    def exportPublicKey(self):
        return self.pub.packb(includeSignature=False)
    
    def pack(self) -> dict:
        data = {
            'userName' : self.name,
            'keyPair'  : self.importedKey
        }
        return data




class Users(dict, metaclass=Singleton):

    def __getitem__(self, __key: str) -> User:
        return super().__getitem__(__key)

    @classmethod
    def load(cls, path : str):
        data = None
        if not os.path.exists(path):
            with open(path, 'wb') as w:
                msgpack.pack({}, w)
            return cls()
        else:
            with open(path, 'rb') as r:
                data = msgpack.unpack(r)
            users = cls()
            if len(data) and isinstance(data, dict):
                for name in data:
                    users[name] = User.unpack(data[name])
            return users

    def save(self, path : str):
        data = {
            name : userData.pack() 
            for name, userData in self.items()
        }
        with open(path, 'wb') as w:
            msgpack.pack(data, w)

