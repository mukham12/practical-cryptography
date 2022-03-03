# Learning about symmetric encryption

# Never use ECB mode, it is not secure
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

key = os.urandom(16)
aesCipher = Cipher(algorithms.AES(key),
                   modes.ECB(),
                   backend=default_backend())

aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()


aesEncryptor.update(b'alice')

#AES operates only on 16 bytes
aesEncryptor.update(b'bob')
aesEncryptor.update(b'bob')
aesEncryptor.update(b'bob')

aesDecryptor.update(_)

# NIST KATS (known answer tests)
# First value of each pair is plaintext
# Second value of each pair is ciphertext 
