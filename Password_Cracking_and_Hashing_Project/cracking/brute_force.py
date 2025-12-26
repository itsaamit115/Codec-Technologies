import itertools, string, hashlib
def brute_force_md5(target_hash, max_length=4):
    chars = string.ascii_lowercase + string.digits
    for length in range(1, max_length + 1):
        for attempt in itertools.product(chars, repeat=length):
            pwd = ''.join(attempt)
            if hashlib.md5(pwd.encode()).hexdigest() == target_hash:
                return pwd
    return None