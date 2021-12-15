from usr.HomeWorkCryptUtil import *
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import ntpath

root = tk.Tk()
root.withdraw()
messagebox.showinfo("Homework by student:1100336",
                    "This Homework made from student 1100336")

PublicKeyPath = filedialog.askopenfilename(title='Public Key Path')
if PublicKeyPath == ():
    exit()
print(PublicKeyPath)
publicKey: int = readKey(PublicKeyPath)

PrivateKeyPath = filedialog.askopenfilename(title='Private Key Path')
if PublicKeyPath == ():
    exit()
privateKey: int = readKey(PrivateKeyPath)

ShareSecret: int = DFFindShareSecret(publicKey, privateKey)
AESKey = getAESKeyFromShareSecret(ShareSecret)

CipherTextPath = filedialog.askopenfilename(title='Cipher text')
if CipherTextPath == ():
    exit()


plainText = AESCBCDecrypt(AESKey, readFileAllBytes(CipherTextPath))

DecryptFilePath = filedialog.asksaveasfile(
    initialfile=CipherTextPath.replace(".cipher",""))

if DecryptFilePath == ():
    exit()

DecryptFilePath:Str=DecryptFilePath.name
if os.path.isfile(DecryptFilePath):os.remove(DecryptFilePath)

writeFileAllBytes(plainText, DecryptFilePath)
