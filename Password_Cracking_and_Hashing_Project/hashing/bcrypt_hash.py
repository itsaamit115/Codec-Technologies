import bcrypt
def bcrypt_hash(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def bcrypt_verify(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)