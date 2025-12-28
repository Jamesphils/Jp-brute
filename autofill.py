import time
import sys
import random
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def slow(text, delay=0.035):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    print("""
############################################################
############################################################
######  ######   #####   ######   ##   ##   ###### ########
##      ##   ## ##   ##  ##   ##  ##   ##   ##   ##   ##
##      ######  ##   ##  ######   #######   ##   ##   ####
##      ##   ## ##   ##  ##   ##  ##   ##   ##   ##   ##
######  ##   ##  #####   ##   ##  ##   ##   ######    ######
############################################################
########################  DARK HOOD  ########################
############################################################
# Status  : FREE
# Creator : Lord Z
# Tool    : Cracker (PERFECT)
# Mode    : Digging
############################################################
""")

def loading_line(label, loops=18):
    sys.stdout.write(f"[{label} == ")
    sys.stdout.flush()
    for _ in range(loops):
        sys.stdout.write("loading...")
        sys.stdout.flush()
        time.sleep(0.15)
        sys.stdout.write("\b" * 10)
    sys.stdout.write("FAILED ]\n")
    sys.stdout.flush()

def fake_tool():
    clear()
    banner()

    slow("[*] Initializing Dark Hood Core Modules...")
    time.sleep(1)

    target = input("\n[?] Enter email or phone number: ")

    slow("\n[+] Target registered")
    slow("[+] Scanning social media footprint...")
    time.sleep(1.2)

    print("\n========== RESULT ==========\n")
    loading_line("Password")
    loading_line("Followers")
    loading_line("Following")
    loading_line("Account Email")
    loading_line("Recovery Token")
    loading_line("Session Cookie")

    time.sleep(1)

    slow("\n[-] PROCESS TERMINATED")
    slow("[-] Reason: Session cookie expired")
    slow("[-] Server returned: 403 Forbidden")
    slow("\n[!] Tip: Update cookies or wait 24 hours")
    slow("[!] Dark Hood shutting down...")
    slow("[!] Stay anonymous.\n")

if __name__ == "__main__":
    fake_tool()