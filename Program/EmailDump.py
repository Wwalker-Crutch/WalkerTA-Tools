"""
Name:
   EmailDump
Author:
    William Walker @ Crutchfield
Description:


Imports:
     @WalkerLog.py
     termcolor --- For colored console output
"""

from termcolor import colored
from WalkerLog import *
import GLOBALS

def SenderAddress():

    GLOBALS.SENDER_ADDRESS = input("\n    Enter sender email address: ").strip()
    if GLOBALS.SENDER_ADDRESS:
        log(f"\n[EMAIL_DUMP] Sender Address Logged: {GLOBALS.SENDER_ADDRESS}")
        print(colored("    ✅ Sender address logged.", "green"))
    else:
        print(colored("    ❌ No input received.\n", "red"))

def FoundEmails():
    print(colored("\n    📥 Enter discovered emails (type 'd' to finish):", "cyan"))
    while True:
        email = input("     ➤ ").strip()
        if email.lower() == "d":
            break
        if email:
            GLOBALS.FOUND_EMAILS.append(email)
            log(f"\n[EMAIL_DUMP] Found Email Added: {email}")
            print(colored("    ✅ Email added.", "green"))
        else:
            print(colored("    ⚠️ Empty input ignored.", "yellow"))


def PrintCollectedEmails():
    print(colored("\n    📄 Collected Email Data:", "blue"))

    print(colored("\n    Sender Address:", "blue"))
    print(f"       {GLOBALS.SENDER_ADDRESS if GLOBALS.SENDER_ADDRESS else 'None'}")

    print(colored("    Found Emails:", "blue"))
    if GLOBALS.FOUND_EMAILS:
        for email in GLOBALS.FOUND_EMAILS:
            print(f"       {email}")
        else:
            print("       None")

def EmailDumpMain():
    print(colored("\n    *-------------------------📨 Email Dump Tool 📨------------------------*", "magenta"))

    choice = input("\n    Sender address, add to discovered emails, print collected emails (s/d/p): ").strip().lower()

    if choice == "s":
        SenderAddress()
    elif choice == "d":
        FoundEmails()
    elif choice == "p":
        PrintCollectedEmails()
    else:
        print(colored("    ❌ Invalid option. Please choose 's', 'd', or 'p'.", "red"))

    print(colored("\n    *----------------------------------------------------------------------*", "magenta"))
