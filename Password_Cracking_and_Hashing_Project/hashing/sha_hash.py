import hashlib
def sha256_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def sha512_hash(password):
    return hashlib.sha512(password.encode()).hexdigest()