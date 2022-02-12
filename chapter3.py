# Learning about symmetric encryption
import os

key = os.urandom(16)

# Never use ECB mode, it is not secure
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
