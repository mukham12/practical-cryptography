from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

key = os.urandom(32)
iv = os.urandom(16)

test_key = bytes.fromhex('00112233445566778899AABBCCDDEEFF')

aesCipher = Cipher(algorithms.AES(test_key),
                   modes.CBC(iv),
                   backend=default_backend())

aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()

# Make a padder/unpadder pair for 128 bit block sizes.
padder = padding.PKCS7(128).padder()
unpadder = padding.PKCS7(128).unpadder()

plaintexts = [
    b'SHORT',
    b'MEDIUM MEDIUM MEDIUM',
    b'LONG LONG LONG LONG LONG LONG',
]

ciphertexts = []

for m in plaintexts:
    padded_message = padder.update(m)
    ciphertexts.append(aesEncryptor.update(padded_message))
    ciphertexts.append(aesEncryptor.update(padder.finalize()))
    print("Recovered", unpadder.update(padded.message())
