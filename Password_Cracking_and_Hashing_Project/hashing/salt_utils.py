import os, hashlib
def generate_salt():
    return os.urandom(16)

def salted_hash(password, salt):
    return hashlib.sha256(salt + password.encode()).hexdigest()