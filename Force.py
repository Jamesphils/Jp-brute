import requests
from bs4 import BeautifulSoup
import re
import os

# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Print the title
print("*" * 50)
print("*                    JP-Brute                    *")
print("*" * 50)
print("Creator: James Phillips")
print("Status: Free")
print("Creation Date: December 4")
print()

# Menu
print("[1] Ping Website          [2] Web Scraping")
print("[3] Web Email Scraping   [4] Web Number Scraping")
print()

# Get user input
choice = input("Enter your choice: ")
url = input("Enter the target website URL: ")

if choice == "1":
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("\033[92m[ Success ] Website is up\033[0m")
        else:
            print("\033[91m[ Failed ] Website is down\033[0m")
    except Exception as e:
        print("\033[91m[ Failed ] Error: ", str(e), "\033[0m")

elif choice == "2":
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print("\033[92m[ Success ] Web scraping successful\033[0m")
        print(soup.text)
    except Exception as e:
        print("\033[91m[ Failed ] Error: ", str(e), "\033[0m")

elif choice == "3":
    try:
        response = requests.get(url)
        emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", response.text)
        if emails:
            print("\033[92m[ Success ] Emails found\033[0m")
            for email in emails:
                print(email)
        else:
            print("\033[91m[ Failed ] No emails found\033[0m")
    except Exception as e:
        print("\033[91m[ Failed ] Error: ", str(e), "\033[0m")

elif choice == "4":
    try:
        response = requests.get(url)
        numbers = re.findall(r'\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}', response.text)
        if numbers:
            print("\033[92m[ Success ] Numbers found\033[0m")
            for number in numbers:
                print(number)
        else:
            print("\033[91m[ Failed ] No numbers found\033[0m")
    except Exception as e:
        print("\033[91m[ Failed ] Error: ", str(e), "\033[0m")

else:
    print("\033[91m[ Failed ] Invalid choice\033[0m")