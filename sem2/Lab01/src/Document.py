from __future__ import annotations
from dataclasses import dataclass
from io import FileIO

from Crypto.Signature import pkcs1_15
from Crypto.Hash import MD5

from User import User

@dataclass
class Document:
    userName  : str
    signature : bytes
    text      : str

    @classmethod
    def unpackb(cls, data : bytes) -> Document:
        bNameLen, data = data[:2], data[2:]
        nameLen = int.from_bytes(bNameLen, byteorder='little', signed=False)
        bSigLen, data = data[:2], data[2:]
        sigLen = int.from_bytes(bSigLen, byteorder='little', signed=False)

        name, data = data[:nameLen], data[nameLen:]
        sig, data = data[:sigLen], data[sigLen:]
        name = name.decode('UTF-8')
        text = data.decode('UTF-8')
        return cls(name, sig, text)

    @classmethod
    def unpack(cls, stream : FileIO):
        data = stream.read()
        return Document.unpackb(data)


    @classmethod
    def fromPlainText(cls, text : str, user : User) -> Document:
        if user.state == User.AccessState.ALLOWED:
            bText = text.encode('UTF-8')
            myhash = MD5.new(bText)
            signature = pkcs1_15.new(user.keys)
            sig = signature.sign(myhash)
            return cls(user.name, sig, text)
        else:
            # return None
            raise ValueError('Passed user does not have access')
            


    def packb(self):
        # Длина имени подписывающего пользователя
        # Длина подписи
        # Имя подписывающего пользователя
        # Электронная подпись
        # Текст документа
        bName = self.userName.encode('UTF-8')
        bNameLen = len(bName).to_bytes(2, byteorder='little', signed=False)
        bSigLen = len(self.signature).to_bytes(2, byteorder='little', signed=False)
        bText = self.text.encode('UTF-8')
        data = bNameLen[:] + bSigLen[:] + bName[:] + self.signature[:] + bText[:]
        return data

    def pack(self, stream : FileIO):
        data = self.packb()
        stream.write(data)
