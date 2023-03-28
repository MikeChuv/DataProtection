from __future__ import annotations
import typing
from dataclasses import dataclass
from io import FileIO

from Crypto.Hash import RIPEMD160
from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA

@dataclass
class PublicKey:
    ownerName : str
    key       : bytes
    signature : typing.Optional[bytes] = None

    @classmethod
    def unpackb(cls, data : bytes) -> PublicKey:
        bNameLen, data = data[:2], data[2:]
        nameLen = int.from_bytes(bNameLen, byteorder='little', signed=False)
        bKeyLen, data = data[:2], data[2:]
        keyLen = int.from_bytes(bKeyLen, byteorder='little', signed=False)

        name, data = data[:nameLen], data[nameLen:]
        key, data = data[:keyLen], data[keyLen:]
        signature = None
        if data:
            signature = data
        return cls(name.decode('UTF-8'), key, signature)

    @classmethod
    def unpack(cls, stream : FileIO):
        data = stream.read()
        return PublicKey.unpackb(data)
    
    def makeSignature(self, secretKey : bytes):
        myhash = RIPEMD160.new(self.key)
        signature = pkcs1_15.new(secretKey)
        self.signature = signature.sign(myhash)

    def isSignatureValid(self, publicKey : RSA.RsaKey):
        if not self.signature:
            return False
        myhash = RIPEMD160.new(self.key)
        signature = pkcs1_15.new(publicKey)
        try:
            signature.verify(myhash, self.signature)
            return True
        except ValueError as e:
            return False

    def packb(self, includeSignature = False) -> bytes:
        bName = self.ownerName.encode('UTF-8')
        bNameLen = len(bName).to_bytes(2, byteorder='little', signed=False)
        publickey = self.key
        bKeyLen = len(publickey).to_bytes(2, byteorder='little', signed=False)
        data = bNameLen[:] + bKeyLen[:] + bName[:] + publickey[:]
        if includeSignature and self.signature:
            data += self.signature
        return data

    def pack(self, stream : FileIO):
        data = self.packb()
        stream.write(data)


