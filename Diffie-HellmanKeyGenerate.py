from usr.HomeWorkCryptUtil import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()
root.withdraw()
messagebox.showinfo("Homework by student:1100336", "This Homework made from student 1100336")
messagebox.showinfo("Generate Diffie-Hellman Key Pair", "Generate Diffie-Hellman Key Pair")

privateKey=DFrandomPrivateKey()
DF=DFSetFromPrivateKey(privateKey)
publicKey=DF.gen_public_key()

PublicKeyPath = (filedialog.asksaveasfile(initialfile = "Diffie-HellmanPublicKey")).name
PrivateKeyPath = (filedialog.asksaveasfile(initialfile = "Diffie-HellmanPrivateKey")).name

if os.path.isfile(PublicKeyPath):os.remove(PublicKeyPath)
if os.path.isfile(PrivateKeyPath):os.remove(PrivateKeyPath)

writeKey(publicKey,PublicKeyPath)
writeKey(privateKey,PrivateKeyPath)