"""
Name:
   EmailDump
Author:
    William Walker @ Crutchfield
Description:
             Collects discovered email addresses from user input.
    Logs entries and prints stored data interactively via console.

Imports:
     @WalkerLog.py
     @GLOBALS.py
     termcolor --- For colored console output
"""

from termcolor import colored
from WalkerLog import *
import GLOBALS

def PromptForSenderFromAddress():
    sender_from = input("\n        📨 Enter Sender-From address (press Enter to skip): ").strip()
    if sender_from:
        GLOBALS.SENDER_FROM = sender_from
        log(f"\n[EMAIL_DUMP] Sender-From Address Set: {GLOBALS.SENDER_FROM}")
        print(colored("        ✅ Sender-From address set.", "green"))
    else:
        print(colored("        ↪️ No Sender-From address provided; skipping.", "yellow"))


def PromptForReturnPath():
    return_path = input("\n        📨 Enter Return-Path address (press Enter to skip): ").strip()
    if return_path:
        GLOBALS.SENDER_RETURN_PATH = return_path
        log(f"\n[EMAIL_DUMP] Return-Path Set: {GLOBALS.SENDER_RETURN_PATH}")
        print(colored("        ✅ Return-Path address set.", "green"))
    else:
        print(colored("        ↪️ No Return-Path address provided; skipping.", "yellow"))


def PromptForSenderAddress():
    sender_input = input("\n        📨 Enter sender address (press Enter to skip): ").strip()
    if sender_input:
        GLOBALS.SENDER_ADDRESS = sender_input
        log(f"\n[EMAIL_DUMP] Sender Address Set: {GLOBALS.SENDER_ADDRESS}")
        print(colored("        ✅ Sender address set.", "green"))
    else:
        print(colored("        ↪️ No sender address provided; skipping.", "yellow"))


def FoundEmails():
    print(colored("\n    📥 Enter discovered emails:", "cyan"))
    PromptForSenderAddress()
    PromptForSenderFromAddress()
    PromptForReturnPath()

    print(colored("\n        📥 Extra Emails Found ('d' to finish):", "cyan"))
    while True:
        email = input("        ➤ ").strip()
        if email.lower() == "d":
            break
        if email:
            GLOBALS.FOUND_EMAILS.append(email)
            log(f"\n[EMAIL_DUMP] Found Email Added: {email}")
            print(colored("        ✅  Email added.", "green"))
        else:
            print(colored("        ⚠️ Empty input ignored.", "yellow"))


def PrintCollectedEmails():
    print(colored("\n    📄 Collected Email Data:", "blue"))

    print(colored("\n    Sender Address:", "blue"))
    print(f"       {GLOBALS.SENDER_ADDRESS if GLOBALS.SENDER_ADDRESS else 'None'}")

    print(colored("    Sender-From Address:", "blue"))
    print(f"       {GLOBALS.SENDER_FROM if GLOBALS.SENDER_FROM else 'None'}")

    print(colored("    Sender-From/Return-Path Address:", "blue"))
    print(f"       {GLOBALS.SENDER_RETURN_PATH if GLOBALS.SENDER_RETURN_PATH else 'None'}")

    print(colored("    Found Emails:", "blue"))
    if GLOBALS.FOUND_EMAILS:
        for email in GLOBALS.FOUND_EMAILS:
            print(f"       {email}")
    else:
        print("       None")

def EmailDumpMain():
    print(colored("\n    *-------------------------📨 Email Dump Tool 📨------------------------*", "magenta"))

    choice = input("\n    Add to discovered emails or Print collected emails (d/p): ").strip().lower()

    if choice == "d":
        FoundEmails()
    elif choice == "p":
        PrintCollectedEmails()
    else:
        print(colored("    ❌ Invalid option. Please choose 'd' or 'p'.", "red"))

    print(colored("\n    *----------------------------------------------------------------------*", "magenta"))
