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

PlainTextPath = filedialog.askopenfilename(title='Plain text')
if PlainTextPath == ():
    exit()


ciph_text = AESCBCEncrypt(AESKey, readFileAllBytes(PlainTextPath))

CipherFilePath = filedialog.asksaveasfile(
    initialfile=ntpath.basename(PlainTextPath)+".cipher")

if CipherFilePath == ():
    exit()

CipherFilePath:Str=CipherFilePath.name
if os.path.isfile(CipherFilePath):os.remove(CipherFilePath)

writeFileAllBytes(ciph_text, CipherFilePath)
