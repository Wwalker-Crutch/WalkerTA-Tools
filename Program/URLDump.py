"""
Name:
   URLDump
Author:
    William Walker @ Crutchfield
Description:
             Collects and sanitizes malicious and credential-harvesting URLs from user input.
    Logs entries and prints stored data interactively via console.

Imports:
     @WalkerLog.py
     @SanitizeURL.py
     @GLOBALS.py
     termcolor --- For colored console output
"""

from termcolor import colored
from WalkerLog import *
import GLOBALS
from SanitizeURL import SanitizeURL


def PromptForMaliciousURL():
    url = input("\n        🌐 Enter Malicious URL (press Enter to skip): ").strip()
    if url:
        sanitized = SanitizeURL(url)
        GLOBALS.MAL_URL = sanitized
        log(f"\n[URL_DUMP] Malicious URL Set: {sanitized}")
        print(colored("        ✅ Malicious URL set.", "green"))
    else:
        print(colored("        ↪️ No Malicious URL provided; skipping.", "yellow"))


def PromptForCredPostURL():
    url = input("\n        🛑 Enter Credential Post URL (press Enter to skip): ").strip()
    if url:
        sanitized = SanitizeURL(url)
        GLOBALS.POST_URL = sanitized
        log(f"\n[URL_DUMP] Credential Post URL Set: {sanitized}")
        print(colored("        ✅ Credential Post URL set.", "green"))
    else:
        print(colored("        ↪️ No Credential Post URL provided; skipping.", "yellow"))


def PromptForExtraURLs():
    print(colored("\n        ➕ Extra Discovered URLs (type 'd' to finish):", "cyan"))
    while True:
        url = input("        ➤ ").strip()
        if url.lower() == "d":
            break
        if url:
            sanitized = SanitizeURL(url)
            GLOBALS.URL_LIST.append(f"DiscoveredURL: {sanitized}")
            log(f"\n[URL_DUMP] Discovered URL Added: {sanitized}")
            print(colored("        ✅ URL added.", "green"))
        else:
            print(colored("        ⚠️ Empty input ignored.", "yellow"))


def PrintCollectedURLs():
    print(colored("\n    🌐 Collected URL Data:", "blue"))

    print(colored("\n    Malicious URL:", "blue"))
    print(f"       {GLOBALS.MAL_URL if GLOBALS.MAL_URL else 'None'}")

    print(colored("    Credential Post URL:", "blue"))
    print(f"       {GLOBALS.POST_URL if GLOBALS.POST_URL else 'None'}")

    print(colored("    Discovered URLs:", "blue"))
    if GLOBALS.URL_LIST:
        for entry in GLOBALS.URL_LIST:
            print(f"       {entry}")
    else:
        print("       None")

    print(colored("    Research Links:", "blue"))
    if GLOBALS.RESEARCH_LINKS:
        for entry in GLOBALS.RESEARCH_LINKS:
            print(f"       {entry}")
    else:
        print("       None")


def PromptForResearchLinks():
    print(colored("\n        🔍 Research Links (type 'd' to finish):", "cyan"))
    while True:
        url = input("        ➤ ").strip()
        if url.lower() == "d":
            break
        if url:
            GLOBALS.RESEARCH_LINKS.append(f"{url}")
            log(f"\n[URL_DUMP] Research Link Added: {url}")
            print(colored("        ✅ Research link added.", "green"))
        else:
            print(colored("        ⚠️ Empty input ignored.", "yellow"))



def URLSpecificGlobals():
    print(colored("\n    🌐 Enter Specific URL Metadata:", "cyan"))

    PromptForMaliciousURL()
    PromptForCredPostURL()



def URLDumpMain():
    print(colored("\n    *-------------------------🌐 URL Dump Tool 🌐--------------------------*", "magenta"))

    choice = input("\n    Add URLs, Research Links, Print collected URLs, or Set MISP Specific URLs (a/r/p/s): ").strip().lower()

    if choice == "a":
        PromptForMaliciousURL()
        PromptForCredPostURL()
        PromptForExtraURLs()
    elif choice == "p":
        PrintCollectedURLs()
    elif choice == "r":
        PromptForResearchLinks()
    elif choice == "s":
        URLSpecificGlobals()
    else:
        print(colored("    ❌ Invalid option. Please choose 'a', 'r', 'p', or 's'.", "red"))

    print(colored("\n    *------------------------------------------------------------------------*", "magenta"))
