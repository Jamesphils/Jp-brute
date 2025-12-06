#!/usr/bin/env python3
"""
Gliter 3.0
"""

import hashlib
import random
import time
import sys

# ANSI colors
PURPLE = "\033[95m"
GREEN  = "\033[92m"
CYAN   = "\033[96m"
YELLOW = "\033[93m"
RESET  = "\033[0m"
BOLD   = "\033[1m"

def colored(text, color):
    return f"{color}{text}{RESET}"

def glitter_title():
    G = [
        " ##### ",
        "#     #",
        "#      ",
        "#  ### ",
        "#    # ",
        "#     #",
        " ##### ",
    ]
    L = [
        "#      ",
        "#      ",
        "#      ",
        "#      ",
        "#      ",
        "#      ",
        "###### ",
    ]
    I = [
        "  ###  ",
        "   #   ",
        "   #   ",
        "   #   ",
        "   #   ",
        "   #   ",
        "  ###  ",
    ]
    T = [
        "#######",
        "   #   ",
        "   #   ",
        "   #   ",
        "   #   ",
        "   #   ",
        "   #   ",
    ]
    E = [
        "#######",
        "#      ",
        "#      ",
        "#####  ",
        "#      ",
        "#      ",
        "#######",
    ]
    R = [
        "###### ",
        "#     #",
        "#     #",
        "###### ",
        "#  #   ",
        "#   #  ",
        "#    # ",
    ]
    rows = []
    for i in range(7):
        row = G[i] + "  " + L[i] + "  " + I[i] + "  " + T[i] + "  " + T[i] + "  " + E[i] + "  " + R[i]
        rows.append(row)
    return "\n".join(rows)

def seed_from(text):
    h = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return int(h[:16], 16)

def show_header():
    print(colored(glitter_title(), PURPLE + BOLD))
    print()
    info = [
        ("Creator", "hacker z"),
        ("Status",  "running"),
        ("Speed",   "5G"),
    ]
    max_label = max(len(lbl) for lbl, _ in info)
    max_val = max(len(val) for _, val in info)
    box_width = max_label + max_val + 7
    top = "#" * box_width
    print(colored(top, GREEN))
    for lbl, val in info:
        line = f"# {lbl.ljust(max_label)} : {val.ljust(max_val)} #"
        print(colored(line, GREEN))
    print(colored(top, GREEN))
    print()
    menu_line1 = "[1] Facebook   [2] Instagram"
    menu_line2 = "[3] X (formerly Twitter)   [4] TikTok"
    print(colored(menu_line1, CYAN + BOLD))
    print(colored(menu_line2, CYAN + BOLD))
    print()

def fake_profile_fields(seed_val, platform):
    rnd = random.Random(seed_val)

    # New: More “real” styled usernames
    first_names = ["James", "Gloria", "Michael", "Stanley", "Sophia", "Daniel", "Kelvin", "Sandra", "Victor", "Janet"]
    last_names  = ["Adams", "Okoro", "Hernandez", "Brown", "Adeyemi", "Stone", "Peters", "Martins", "Lee", "Johnson"]

    uname = f"{first_names[rnd.randint(0,9)]}{last_names[rnd.randint(0,9)]}{rnd.randint(10,99)}"

    pw_words = ["sun","blue","node","alpha","delta","neo","seed","orbit","echo"]
    password = pw_words[rnd.randint(0, len(pw_words)-1)] + str(rnd.randint(10,999))

    friends = f"{rnd.randint(1,9)}.{rnd.randint(0,9)}k" if rnd.random() < 0.6 else f"{rnd.randint(10,9999)}"
    years = f"{rnd.randint(0,12)} years"
    created_year = str(2010 + rnd.randint(0,15))
    uid = rnd.randint(1000000,99999999)

    bio_snippets = [
        "Loves coffee and code",
        "Collector of odd usernames",
        "Occasional memer",
        "Private profile",
        "Active poster"
    ]
    bio = rnd.choice(bio_snippets)

    return {
        "Username": uname,
        "Password": password,
        "User friends": friends,
        "Account years": years,
        "Created": created_year,
        "UID": str(uid),
        "Bio": bio
    }

def print_fake_report(platform, target_input):
    seed_val = seed_from(platform + "|" + target_input)
    fields = fake_profile_fields(seed_val, platform)

    heading = f"{platform.upper()} HACK"
    print(colored("=" * max(20, len(heading)), YELLOW))
    print(colored(heading.center(40), YELLOW + BOLD))
    print(colored("=" * max(20, len(heading)), YELLOW))
    print()

    steps = ["Opening interface", "Scraping public metadata", "Assembling profile", "Rendering report"]
    for s in steps:
        sys.stdout.write(colored(f"[{s}] ", GREEN))
        sys.stdout.flush()
        time.sleep(0.18)
        print(colored("OK", GREEN))
    print()

    idx = 0
    for k, v in fields.items():
        idx += 1
        code = (seed_val >> (idx*4)) & 0xFFFFFFFF
        print(colored(f"[ {k} ] = {code} = [ {v} ]", GREEN))
    print()

    print(colored("This output is generated locally and is for entertainment/educational use only.", CYAN))
    print(colored("Do not enter real emails, phone numbers, passwords, or other sensitive information.", CYAN))
    print()

def platform_flow(choice):
    mapping = {
        "1": "Facebook",
        "2": "Instagram",
        "3": "X",
        "4": "TikTok"
    }
    platform = mapping.get(choice)
    if not platform:
        print(colored("Invalid choice. Pick 1, 2, 3 or 4.", YELLOW))
        return
    print()
    print(colored(f"--- {platform.upper()} CONSOLE ---", PURPLE))
    print(colored("Enter target identifier ( phone number or E-mail). Example: user@email.com or +211 07653235542 ", CYAN))

    target = input(colored("Target> ", GREEN)).strip()
    if not target:
        target = f"demo_{platform.lower()}"
        print(colored(f"No input. Using fallback identifier: {target}", YELLOW))

    print()
    print_fake_report(platform, target)

def main():
    show_header()
    print(colored("Which number do you want to input? (1-4)  Type q to quit.", CYAN))

    while True:
        choice = input(colored("Choice> ", GREEN)).strip().lower()
        if choice in ("q", "quit", "exit"):
            print(colored("Goodbye.", PURPLE))
            break
        platform_flow(choice)
        print(colored("Back to menu. Choose another (1-4) or q to quit.", CYAN))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + colored("Interrupted. Exiting.", YELLOW))