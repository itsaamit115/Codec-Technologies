import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.sha_algorithms import sha256_hash, sha512_hash
from src.aes_algorithm import aes_encrypt, aes_decrypt
from src.rsa_algorithm import generate_keys, rsa_encrypt, rsa_decrypt
from Crypto.Random import get_random_bytes

print("==== SHA DEMO ====")
print("SHA-256:", sha256_hash("password123"))
print("SHA-512:", sha512_hash("password123"))

print("\n==== AES DEMO ====")
key = get_random_bytes(16)
iv, ciphertext = aes_encrypt(key, "Hello AES Encryption")
print("Decrypted:", aes_decrypt(key, iv, ciphertext))

print("\n==== RSA DEMO ====")
private_key, public_key = generate_keys()
ciphertext = rsa_encrypt(public_key, "Hello RSA Encryption")
print("Decrypted:", rsa_decrypt(private_key, ciphertext))