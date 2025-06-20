"""
Name:
   GLOBALSPrint
Author:
    William Walker @ Crutchfield
Description:
             Prints and shows everything the program has accumulated so far

Imports:
     @GLOBALS.py
     termcolor --- For colored console output
"""
from termcolor import colored
import GLOBALS

def GLOBALSPrintMain():
    print(colored("\n    *---------------------🌐 GLOBALS STATUS REPORT 🌐----------------------*", "cyan"))

    print(colored("\n    ✉️  Email Metadata:", "magenta"))
    print(f"    - Sender Address: {GLOBALS.SENDER_ADDRESS or ''}")
    print(f"    - Sender Display: {GLOBALS.SENDER_DISPLAY or ''}")
    print(f"    - Sender Subject: {GLOBALS.SENDER_SUBJECT or ''}")
    print(f"    - Sender IP: {GLOBALS.SENDER_IP or ''}")
    print(f"    - Sender From: {GLOBALS.SENDER_FROM or ''}")
    print(f"    - Return Path: {GLOBALS.SENDER_RETURN_PATH or ''}")

    print(colored("\n    📁 Files:", "magenta"))
    print(f"    - FILES: {GLOBALS.FILES if GLOBALS.FILES else ''}")

    print(colored("\n    🌐 URLs & Links:", "magenta"))
    print(f"    - Malicious URL: {GLOBALS.MAL_URL or ''}")
    print(f"    - Post URL: {GLOBALS.POST_URL or ''}")
    print(f"    - URL List: {GLOBALS.URL_LIST if GLOBALS.URL_LIST else ''}")
    print(f"    - Research Links: {GLOBALS.RESEARCH_LINKS if GLOBALS.RESEARCH_LINKS else ''}")

    print(colored("\n    🧠 IP Mapping:", "magenta"))
    if GLOBALS.IP_LIST:
        for title, ip in GLOBALS.IP_LIST.items():
            print(f"    - {title}: {ip}")
    else:
        print("    ❌ No IP entries.")

    print(colored("\n    🔁 Redirect Chains:", "magenta"))
    if GLOBALS.RCHAINLIST:
        for idx, chain in enumerate(GLOBALS.RCHAINLIST):
            traced = "\n        --> ".join(chain)
            print(f"\n    [{idx}] Redirect Path:\n        {traced}")
    else:
        print("    ❌ No redirect chains created.")

    print(colored("\n    *----------------------------------------------------------------------*\n", "cyan"))
