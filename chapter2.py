import hashlib

md5hasher = hashlib.md5()
md5hasher.hexdigest()

md5hasher = hashlib.md5(b'alice')
