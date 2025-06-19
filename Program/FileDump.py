"""
Name:
   FileDump
Author:
    William Walker @ Crutchfield
Description:
             Collects discovered file names from user input with SHA256SUM hashes.

Imports:
     @WalkerLog.py
     @GLOBALS.py
     @SHA256.py
     termcolor --- For colored console output
"""

from termcolor import colored
from WalkerLog import *
import GLOBALS
from SHA256Sum import SHA256FromFile, SHA256FromPlaintext


def FoundFiles():
    print(colored("\n    📥 Add file entries (type 'd' to finish):", "cyan"))
    while True:
        choice = input("\n    ➤ Use file explorer or plaintext filename? (f/p/d): ").strip().lower()
        if choice == "d":
            break
        elif choice == "f":
            result = SHA256FromFile()
        elif choice == "p":
            result = SHA256FromPlaintext()
        else:
            print(colored("    ❌ Invalid input. Type 'f', 'p', or 'd'.", "red"))
            continue

        if result:
            GLOBALS.FILES.append(result)
            print(colored("    ✅ File entry added.", "green"))
            log(f"\n[FILES_DUMP] Found File Added: {result}")
        else:
            print(colored("    ⚠️ Entry not added due to error or invalid input.", "yellow"))


def PrintCollectedFiles():
    print(colored("\n    📄 Collected File Data:", "blue"))
    if GLOBALS.FILES:
        for file in GLOBALS.FILES:
            print(f"       {file}")
    else:
        print("       None")


def FileDumpMain():
    print(colored("\n    *--------------------------📁 File Dump Tool 📁-------------------------*", "magenta"))
    choice = input("\n    Add file hashes or Print collected data (f/p): ").strip().lower()

    if choice == "f":
        FoundFiles()
    elif choice == "p":
        PrintCollectedFiles()
    else:
        print(colored("    ❌ Invalid option. Please choose 'a' or 'p'.", "red"))

    print(colored("\n    *------------------------------------------------------------------------*", "magenta"))
