from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

aesCipher = 
class EncryptionManager:
    self.key = os.urandom(32)
    self.iv = os.urandom(16)

    def encrypt_message(self, message):
        encryptor = Cipher(algorithms.AES(test_key),
                           modes.EBC(),
                           backend=default_backend())

