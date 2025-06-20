"""
Name:
   IPDump
Author:
    William Walker @ Crutchfield
Description:
             Collects sender IP and additional discovered IPs from user input.
             Logs entries and prints stored data interactively via console.

Imports:
     @WalkerLog.py
     @GLOBALS.py
     termcolor --- For colored console output
"""
from termcolor import colored
from WalkerLog import *
import GLOBALS


def PromptForSenderIP():
    sender_ip = input("\n        🌐 Enter Sender IP (press Enter to skip): ").strip()
    if sender_ip:
        GLOBALS.SENDER_IP = sender_ip
        log(f"\n[IP_DUMP] Sender IP Set: {GLOBALS.SENDER_IP}")
        print(colored("        ✅ Sender IP set.", "green"))
    else:
        print(colored("        ↪️ No Sender IP provided; skipping.", "yellow"))



def PromptForDiscoveredIPs():
    print(colored("\n        ➕ Extra Discovered IPs (type 'd' to finish):", "cyan"))
    while True:
        label = input("        🏷️ Title/Context for IP (e.g., SuspiciousSrc): ").strip()
        if label.lower() == "d":
            break

        ip = input("        🌐 Enter corresponding IP address: ").strip()
        if ip.lower() == "d":
            break

        if ip:
            GLOBALS.IP_LIST[label] = ip
            log(f"\n[IP_DUMP] Discovered IP Added: {label} → {ip}")
            print(colored("        ✅ IP entry added.", "green"))
        else:
            print(colored("        ⚠️ Empty IP input ignored.", "yellow"))

def PrintCollectedIPs():
    print(colored("\n    🌐 Collected IP Data:", "blue"))

    print(colored("\n    Sender IP:", "blue"))
    print(f"       {GLOBALS.SENDER_IP if GLOBALS.SENDER_IP else 'None'}")

    print(colored("    Discovered IPs with Titles:", "blue"))
    if GLOBALS.IP_LIST:
        for label, ip in GLOBALS.IP_LIST.items():
            print(f"       {label}: {ip}")
    else:
        print("       None")


def IPSpecificGlobals():
    print(colored("\n    🌐 Enter Specific IP Metadata:", "cyan"))

    PromptForSenderIP()

def IPDumpMain():
    print(colored("\n    *--------------------------📡 IP Dump Tool 📡--------------------------*", "magenta"))

    choice = input("\n    Add IPs, Print collected IPs, or Set sender IP only (a/p/s): ").strip().lower()

    if choice == "a":
        PromptForSenderIP()
        PromptForDiscoveredIPs()
    elif choice == "p":
        PrintCollectedIPs()
    elif choice == "s":
        IPSpecificGlobals()
    else:
        print(colored("    ❌ Invalid option. Please choose 'a' or 'p'.", "red"))

    print(colored("\n    *------------------------------------------------------------------------*", "magenta"))
