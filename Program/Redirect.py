"""

UNDER CONSTRUCTION

"""
from termcolor import colored
from SanitizeURL import SanitizeURL
from WalkerLog import log
from GLOBALS import RCHAINLIST

def PrintRedirectChains():
    print(colored("\n    📦 Current Redirect Chains:\n", "yellow"))
    if not RCHAINLIST:
        print("    (No redirect chains found.)\n")
        return
    for idx, chain in enumerate(RCHAINLIST):
        print(colored(f"    [{idx}]\n    {TraceRedirectChain(chain)}\n", "yellow"))


def TraceRedirectChain(chain):
    return "\n        ------Redirect----->\n    ".join(chain)

def NewRedirectChain():
    PrintRedirectChains()
    print(colored("    🔗 Start a new redirect chain\n", "cyan"))
    url1 = input("    Enter original URL: ").strip()
    url2 = input("    Enter redirect target: ").strip()
    log(f"\n [INPUT_REDIRECT1] User 1st URL Input {url1}")
    log(f"\n [INPUT_REDIRECT2] User 2nd URL Input {url2}")

    sanitized1 = SanitizeURL(url1)
    sanitized2 = SanitizeURL(url2)

    new_chain = [sanitized1, sanitized2]
    RCHAINLIST.append(new_chain)

    chain_display = TraceRedirectChain(new_chain)
    log(f"\n[NEW_REDIRECT] Created new redirect chain:\n    {chain_display}")
    print(colored(f"\n    ✅  Redirect Chain Created:\n\n    {chain_display}\n", "green"))

def ExtendRedirectChain():
    print(colored("\n    ➕ Extend a redirect chain from the last URL\n", "cyan"))

    if not RCHAINLIST:
        print(colored("    ❌ No redirect chains exist yet.\n", "red"))
        return

    PrintRedirectChains()

    try:
        index = int(input("\n    Enter the index of the chain to extend: ").strip())
        if index < 0 or index >= len(RCHAINLIST):
            raise ValueError
    except ValueError:
        print(colored("    ❌ Invalid index. Please enter a valid number.\n", "red"))
        return
    url = input("    Enter Redirect URL: ").strip()
    sanitized_url = SanitizeURL(url)

    RCHAINLIST[index].append(sanitized_url)

    chain_display = TraceRedirectChain(RCHAINLIST[index])

    log(f"\n[CHAIN_EXTEND] Updated chain {index}:\n    {chain_display}")

    print(colored(f"\n    🔄 Redirect Chain Updated:\n\n    {chain_display}\n", "green"))

def RedirectMain():
    print(colored("\n    *----------------------🚦Redirect Chain Builder🚦----------------------*", "magenta"))
    mode = input("\n    New redirect, Extend existing, or Print chains (n/e/p): ").strip().lower()
    if mode == "n":
        NewRedirectChain()
    elif mode == "e":
        ExtendRedirectChain()
    elif mode == "p":
        PrintRedirectChains()
    else:
        print(colored("    ❌ Invalid option. Returning to menu.", "red"))
    print(colored("\n    *----------------------------------------------------------------------*", "magenta"))
