import requests
from bs4 import BeautifulSoup
import re
import os

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# Colored Thick JP‑BRUTE ASCII Header
print("\033[1;92m")  # Bold Green
print("######################################################")
print("#####   ######   ########   #####   #####   ##########")
print("#####   ######   ########   #####   #####   ##   #####")
print("#####   ##       ##         ## ##   ## ##   ##   #####")
print("#####   ######   #######    ##  ##  ##  ##  ##########")
print("#####   ##       ##         ##   ## ##   ## ##   ##  #")
print("#####   ##       ##         ##    ####    ## ##    ## #")
print("#####   ##       ########   ##     ##     ## ##     ###")
print("######################################################")
print("\033[0m")  # Reset color

print("\033[1;94mCreator:\033[0m James Phillips")
print("\033[1;94mStatus:\033[0m Free Project")
print("\033[1;94mCreation Date:\033[0m December 4")
print()

print("\033[1;93m[1] Website Status (Ping)\033[0m")
print("\033[1;93m[2] Web Page Text (Scrape)\033[0m")
print("\033[1;93m[3] Extract Emails\033[0m")
print("\033[1;93m[4] Extract Phone Numbers\033[0m")
print()

choice = input("Enter your choice: ")
url = input("\nEnter your target website URL: ")

print("\n")

if choice == "1":
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("\033[92m✔ Website is Accessible\033[0m")
        else:
            print("\033[91m✘ Website returned error:\033[0m", response.status_code)
    except Exception as e:
        print("\033[91mError:\033[0m", e)

elif choice == "2":
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print("\033[92m✔ Web Page Loaded\033[0m\n")
        print(soup.text[:500])
    except Exception as e:
        print("\033[91mError:\033[0m", e)

elif choice == "3":
    try:
        response = requests.get(url)
        emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", response.text)

        if emails:
            print("\033[92m✔ Emails Found:\033[0m")
            for email in emails:
                print(email)
        else:
            print("\033[91m✘ No Emails Found\033[0m")
    except Exception as e:
        print("\033[91mError:\033[0m", e)

elif choice == "4":
    try:
        response = requests.get(url)
        numbers = re.findall(r"\+?\d[\d\s\-]{6,15}", response.text)

        if numbers:
            print("\033[92m✔ Numbers Found:\033[0m")
            for number in numbers:
                print(number)
        else:
            print("\033[91m✘ No Numbers Found\033[0m")
    except Exception as e:
        print("\033[91mError:\033[0m", e)

else:
    print("\033[91mInvalid Option!\033[0m")