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
