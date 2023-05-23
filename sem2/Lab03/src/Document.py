from __future__ import annotations
from dataclasses import dataclass
from io import FileIO
import OpenSSL.crypto

@dataclass
class Document:
    cert      : OpenSSL.crypto.X509
    signature : bytes
    text      : str

    @classmethod
    def unpackb(cls, data : bytes) -> Document:
        bCertLen, data = data[:2], data[2:]
        certLen = int.from_bytes(bCertLen, byteorder='little', signed=False)
        bSigLen, data = data[:2], data[2:]
        sigLen = int.from_bytes(bSigLen, byteorder='little', signed=False)

        bCert, data = data[:certLen], data[certLen:]
        sig, data = data[:sigLen], data[sigLen:]
        cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, bCert)
        text = data.decode('UTF-8')
        return cls(cert, sig, text)

    @classmethod
    def unpack(cls, stream : FileIO):
        data = stream.read()
        return Document.unpackb(data)


    @classmethod
    def fromPlainText(cls, text : str, pkcs12 : OpenSSL.crypto.PKCS12) -> Document:
        bText = text.encode('UTF-8')
        sig = OpenSSL.crypto.sign(pkcs12.get_privatekey(), bText, 'SHA1')
        return cls(pkcs12.get_certificate(), sig, text)
        # raise ValueError('Passed user does not have access')
            
    def verify(self):
        try:
            OpenSSL.crypto.verify(self.cert, self.signature, self.text, 'SHA1')
            return True
        except Exception as e:
            return False


    def packb(self):
        # Длина сертификата
        # Длина подписи
        # Имя подписывающего пользователя
        # Электронная подпись
        # Текст документа
        bCert = OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, self.cert)
        bCertLen = len(bCert).to_bytes(2, byteorder='little', signed=False)
        bSigLen = len(self.signature).to_bytes(2, byteorder='little', signed=False)
        bText = self.text.encode('UTF-8')
        data = bCertLen[:] + bSigLen[:] + bCert[:] + self.signature[:] + bText[:]
        return data

    def pack(self, stream : FileIO):
        data = self.packb()
        stream.write(data)
