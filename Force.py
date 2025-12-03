# brute_force.py
import itertools
import string
import hashlib
import time

# JP Brute Banner
print("""
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
| | | | | | | | | | | | | | | | | | | | |
| |_| | |_| | |_| | |_| | |_| | |_| | |_|
|  J  P  B  R  U  T  E  H  A  C  K  E  R  |
|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|
""")

# Hash to crack
target_hash = "5f4dcc3b5aa765d61d8327deb882cf99"  # Example MD5 hash

def brute_force_crack(target_hash, max_length=8):
    chars = string.ascii_letters + string.digits
    attempts = 0
    start_time = time.time()
    for length in range(1, max_length + 1):
        for attempt in itertools.product(chars, repeat=length):
            attempt = ''.join(attempt)
            attempt_hash = hashlib.md5(attempt.encode()).hexdigest()
            attempts += 1
            print(f"\rAttempt {attempts}: {attempt} | Hash: {attempt_hash}", end='')
            if attempt_hash == target_hash:
                print(f"\n\nPassword found: {attempt}")
                print(f"Time taken: {time.time() - start_time:.2f} seconds")
                return
    print("\nPassword not found.")

brute_force_crack(target_hash)