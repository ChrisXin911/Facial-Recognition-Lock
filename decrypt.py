#Created by Andre Menezes
#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

#Finding files to encrypt
files = []
for file in os.listdir():
    if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

#Reading the encrytion key
with open("thekey.key", "rb") as key:
    secretkey = key.read()

#Writing back the original content to the files
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)

print("All your files have been decrypted")