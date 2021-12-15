# pip3 install  PyCryptodome
# pip3 install  pyDH
from ast import Bytes, Str
from codecs import utf_16_be_decode
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util import Counter
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import hashlib
import os
import string
import random
import pyDH
import base64
from Crypto.Util.Padding import unpad, pad


def randomAESKey():
    return get_random_bytes(32)


def hash256(KeyStr: Str):
    byteString = bytes(KeyStr, "utf-8")
    hashObj = hashlib.sha256()
    hashObj.update(byteString)
    return hashObj.digest()


def AESCBCEncrypt(key: Bytes, data: Bytes):
    iv = b'l!D\xcf\xca`\xed`\xe2(o\xc9\x84\xa6\xf6\xb3'
    hashObj = hashlib.sha256()
    hashObj.update(key)
    cipher = AES.new(hashObj.digest(), AES.MODE_CBC, iv)
    return cipher.encrypt(pad(data, AES.block_size))


def AESCBCDecrypt(key: Bytes, data: Bytes):
    iv = b'l!D\xcf\xca`\xed`\xe2(o\xc9\x84\xa6\xf6\xb3'
    hashObj = hashlib.sha256()
    hashObj.update(key)
    cipher = AES.new(hashObj.digest(), AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(data), AES.block_size)


def DFrandomPrivateKey():
    DF = pyDH.DiffieHellman()
    return DF.get_private_key()


def DFSetFromPrivateKey(privateLkey: int):
    DF = pyDH.DiffieHellman()
    DF._DiffieHellman__a = privateLkey
    return DF


def DFFindShareSecret(PublicKey: int, PrivateKey: int):
    DF = DFSetFromPrivateKey(PrivateKey)
    return DF.gen_shared_key(PublicKey)


def writeKey(Key: int, filePath):
    with open(filePath, "w") as f:
        f.write(str(Key))
        f.close()


def readKey(filePath):
    key: Str
    with open(filePath, "r") as f:
        key = f.read()
        f.close()
    return int(key)


def getAESKeyFromShareSecret(ShareSecret: int):
    return hash256(str(ShareSecret))


def readFileAllBytes(fileName):
    key = bytes()
    with open(fileName, "rb") as f:
        key = f.read()
        f.close()
    return key


def writeFileAllBytes(byteMsg: Bytes, fileName: Str):
    with open(fileName, "wb") as f:
        f.write(byteMsg)
        f.close()

# def writeByte(byteMsg, fileName):
#     with open(fileName, "ab+") as f:
#         f.write(byteMsg)
#         f.close()


# def readKeyFile(fileName):
#     key=bytes()
#     with open(fileName, "rb") as f:
#         key = f.read()
#         f.close()
#     return key


# def encrptoFile(InputFileName, outputFileName, RSAPublicKey):
#     fileIOBlockSize=1024*1024*128
#     if os.path.isfile(outputFileName):
#         os.system("rm "+outputFileName)
#     # AES
#     key = hash256(randomAESKey())
#     print("AES key in crpto", key, "\n")
#     cipherAESkey = RSAencrypto(key, RSAPublicKey)
#     print("Cipher AES key in crpto:")
#     print(cipherAESkey, "\n")
#     writeByte(cipherAESkey, outputFileName)
#     # AES
#     with open(InputFileName, "rb") as f:
#         fBytes = f.read(fileIOBlockSize)
#         writeByte(encrptoBytes(fBytes, key), outputFileName)
#         while fBytes:
#             fBytes = f.read(fileIOBlockSize)
#             writeByte(encrptoBytes(fBytes, key), outputFileName)
#         f.close()


# def decrptoFile(InputFileName, outputFileName, RSAPrivateKey):
#     fileIOBlockSize=1024*1024*128
#     if os.path.isfile(outputFileName):
#         os.system("rm "+outputFileName)
#     print(InputFileName,RSAPrivateKey)
#     key = RSAdecrypto(readCipherAESkey(InputFileName), RSAPrivateKey)
#     print("AES key recover:", key, "\n")
#     with open(InputFileName, "rb") as f:
#         f.seek(256, 1)
#         bytes = f.read(fileIOBlockSize)
#         print(bytes)
#         writeByte(decrptoBytes(bytes, key), outputFileName)
#         while bytes:
#             bytes = f.read(fileIOBlockSize)
#             writeByte(decrptoBytes(bytes, key), outputFileName)
#         f.close()


# def RSAKeyPair():
#     key = RSA.generate(2048)
#     privateKey = key.exportKey()
#     publicKey = key.publickey().exportKey()
#     keyPair: list = [publicKey, privateKey]
#     return keyPair


# def RSAencrypto(AESkey: bytes, publicKey: bytes):
#     cipherRSA = PKCS1_OAEP.new(RSA.importKey(publicKey))
#     cipherAESkey = cipherRSA.encrypt(AESkey)
#     return cipherAESkey


# def RSAdecrypto(cipherAESkey: bytes, privateKey: bytes):
#     cipherRSA = PKCS1_OAEP.new(RSA.importKey(privateKey))
#     AESkey = cipherRSA.decrypt(cipherAESkey)
#     return AESkey


# def readCipherAESkey(InputFileName):
#     with open(InputFileName, "rb") as f:
#         bytes = f.read(256)
#         f.close()
#         return bytes
