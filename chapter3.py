# Learning about symmetric encryption

# Never use ECB mode, it is not secure
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
