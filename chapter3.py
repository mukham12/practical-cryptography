from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

key = os.urandom(16)

aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()

nist_kats = [('f34481ec3cc627bacd5dc3fb08f273e6',
              '0336763e966d92595a567cc9ce537f5e'),
            ]

# Alice and Bob's shared secret key
test_key = bytes.fromhex('00000000000000000000000000000000')

aesCipher = Cipher(algorithms.AES(test_key),
                   modes.ECB(),
                   backend=default_backend())

aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()

message = b''''''
