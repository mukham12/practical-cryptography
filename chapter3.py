from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

key = os.urandom(32)
iv = os.urandom(16)

aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()

test_key = bytes.fromhex('00112233445566778899AABBCCDDEEFF')

aesCipher = Cipher(algorithms.AES(test_key),
                   modes.CBC(iv),
                   backend=default_backend())

aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()

