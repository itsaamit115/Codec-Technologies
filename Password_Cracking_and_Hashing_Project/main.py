from hashing.md5_hash import md5_hash
from hashing.sha_hash import sha256_hash, sha512_hash
from hashing.bcrypt_hash import bcrypt_hash, bcrypt_verify
from hashing.salt_utils import generate_salt, salted_hash
from cracking.brute_force import brute_force_md5

password = "123"

print("Original Password:", password)
print("MD5:", md5_hash(password))
print("SHA-256:", sha256_hash(password))
print("SHA-512:", sha512_hash(password))

bcrypt_h = bcrypt_hash(password)
print("bcrypt Hash:", bcrypt_h)
print("bcrypt Verify:", bcrypt_verify(password, bcrypt_h))

salt = generate_salt()
print("Salted SHA-256:", salted_hash(password, salt))

print("Cracked Password:", brute_force_md5(md5_hash(password)))