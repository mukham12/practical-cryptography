import hashlib
import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend

md5hasher = hashlib.md5()
md5hasher.hexdigest()

md5hasher = hashlib.md5(b'alice')
md5hasher.hexdigest()

md5hasher = hashlib.md5(b'bob')
md5hasher.hexdigest()

md5hasher = hashlib.md5()
md5hasher.update(b'a')
md5hasher.update(b'l')
md5hasher.update(b'i')
md5hasher.update(b'c')
md5hasher.update(b'e')
md5hasher.hexdigest()

# Learning SHA-1 hash function
hashlib.sha1(b'alice').hexdigest()
hashlib.sha1(b'bob').hexdigest()

# Learning SHA-256 hash function 
hashlib.sha256(b'alice').hexdigest()
hashlib.sha256(b'bob').hexdigest()

# Learning Scrypt
salt = os.urandom(16)

kdf = Scrypt(salt = salt, length = 32,
             n = 2**14, r=8, p=1,
             backend=default_backend())

key = kdf.derive(b'some password')

# Verifying the key
kdf.verify()
