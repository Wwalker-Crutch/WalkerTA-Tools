"""

UNDER CONSTRUCTION

"""
from termcolor import colored
from SanitizeURL import SanitizeURL
from WalkerLog import log

GRAPH = {}

def trace_redirect_chain(start_url):
    chain = [start_url]
    while chain[-1] in GRAPH:
        chain.append(GRAPH[chain[-1]])
    return "\n    ------Redirect----->\n    ".join(chain)

def NewRedirectChain():
    print(colored("\n    🔗 Start a new redirect chain\n", "cyan"))
    url1 = input("    Enter original URL: ").strip()
    url2 = input("    Enter redirect target: ").strip()
    log(f"\n [INPUT_REDIRECT1] User 1st URL Input {url1}")
    log(f"\n [INPUT_REDIRECT2] User 2nd URL Input {url2}")


    sanitized1 = SanitizeURL(url1)
    sanitized2 = SanitizeURL(url2)

    GRAPH[sanitized1] = sanitized2
    log(f"\n [NEW_REDIRECT] Created new redirect: {sanitized1} -> {sanitized2}")

    chain_display = trace_redirect_chain(sanitized1)
    print(colored(f"\n    ✅ Redirect Chain Created:\n\n    {chain_display}\n", "green"))


def ExtendRedirectChain():
    print(colored("\n    ➕ Extend a redirect chain from the tail\n", "cyan"))

    url1 = input("    Enter the LAST URL in the chain: ").strip()
    url2 = input("    Enter Redirect URL: ").strip()

    log(f"\n [INPUT_REDIRECT_EXTEND1] User last URL in chain: {url1}")
    log(f"\n [INPUT_REDIRECT_EXTEND2] User redirect target: {url2}")

    sanitized_url1 = SanitizeURL(url1)
    sanitized_url2 = SanitizeURL(url2)

    GRAPH[sanitized_url1] = sanitized_url2
    log(f"\n [CHAIN_EXTEND] Appended redirect: {sanitized_url1} → {sanitized_url2}")

    root = next((k for k, v in GRAPH.items() if v == sanitized_url2), sanitized_url1)
    while True:
        prev = next((k for k, v in GRAPH.items() if v == root), None)
        if not prev:
            break
        root = prev
    chain_display = trace_redirect_chain(root)

    print(colored(f"\n    🔄 Redirect Chain Updated:\n\n    {chain_display}\n", "green"))


def RedirectMain():
    print(colored("\n    🚦 Redirect Chain Builder", "magenta"))
    mode = input("\n    New redirect or Extend existing? ").strip().lower()
    if mode == "n":
        NewRedirectChain()
    elif mode == "e":
        ExtendRedirectChain()
    else:
        print(colored("    ❌ Invalid option. Returning to menu.", "red"))
