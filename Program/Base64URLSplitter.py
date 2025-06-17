"""
Name:
    Base64URLSplitter
Author:
    William Walker @ Crutchfield
Description:
        Executes when a user wants to split and decode a URL containing encoded
    segments. This command splits and decodes Base64 or Base64URL-encoded
    portions of the URL, providing a clearer view of the underlying data.

        Optionally.... Sensitive elements can be replaced with generic placeholders
    to avoid tracking or identifying entities—e.g., YOUR_COMPANY, ANON_USER,
    honeypot@email.com, or YOUR_NAME.

imports:
    @WalkerLog.py
    @base64Decode.py
    @Base64Encode.py
    @SanitizeURL.py
    termcolor ----> for colored text
    re -----> for regular expressions to match base64 and splitting strings
    pyperclip ---> for clipboard
"""
import re
from WalkerLog import log
from Base64Decode import DecodeBase64String
from termcolor import colored
from Base64Encode import EncodeBase64String
import pyperclip
from SanitizeURL import SanitizeURL


def IsItBase64(s):
    try:
        decoded = DecodeBase64String(s + '=' * ((4 - len(s) % 4) % 4))
        return decoded and not decoded.startswith("❌")
    except:
        return False

def SegmentDecode(base64Parts):
    if not base64Parts:
        print(colored("\n    🔎 No Base64-style candidates found.\n", "red"))
        log("\n[NO_SPLIT] No Base64-style segments found in input URL.")
        return

    print("\n    🧩 Decoded Segments:\n")
    for i, segment in enumerate(base64Parts, 1):
        b64_clean = segment.replace('-', '+').replace('_', '/')
        padded = b64_clean + '=' * ((4 - len(b64_clean) % 4) % 4)
        decoded = DecodeBase64String(padded)
        log(f"\n[SPLIT] Segment {i}: {padded} → {decoded}")
        print(f"    {i}. {colored(padded, 'yellow')}  ----->  {colored(decoded, 'green')}")
    print()



def SplitURL(url):
    parts = re.split(r"[\/\?=&.#]+", url)

    base64Ish = re.compile(r'^[A-Za-z0-9_\-+/]{4,}$')

    base64Parts = [p for p in parts if base64Ish.fullmatch(p) and IsItBase64(p)]

    SegmentDecode(base64Parts)

    return base64Parts


def URLReplace(base64Parts, url):
    modified_url = url


    print(colored("\n        *-----------------🔄Base64 Replacement Mode🔄-----------------*\n", "cyan"))
    for original in base64Parts:
        padded = original + '=='
        originalDecoded = DecodeBase64String(padded)
        choice = input(f"        Replace \"{originalDecoded}\" with new content? (y/n): ").strip().lower()

        if choice == "y":
            new_value = input("\n        Enter new value to encode → ").strip()
            encoded = EncodeBase64String(new_value)
            encoded_url_safe = encoded.replace('+', '-').replace('/', '_').rstrip('=')
            modified_url = modified_url.replace(original, encoded_url_safe)
            log(f"\n[REPLACE] Replaced {original} with {encoded_url_safe}")
            print(f"        ✅  {colored(original, 'red')} → {colored(encoded_url_safe, 'cyan')}"+"\n")
        else:
            print(f"\n        ⚠️  Skipping {colored(original, 'yellow')}"+"\n")

    print(colored(f"        ✅  Final Updated URL: {modified_url}\n", "green"))

    sanitized = SanitizeURL(modified_url)
    print(colored(f"        🔒 Sanitized URL: {sanitized}", "green"))
    log(f"[REPLACE] Final modified URL: {sanitized}")

    pyperclip.copy(sanitized)
    print(colored("        📋 Sanitized URL copied to clipboard", "green"))

    print(colored("\n        *-------------------------------------------------------------*\n", "cyan"))


def Base64URLSplitterMain():
    print(colored("\n    *-----------------🗂️ Base64 URL Splitter/Replacer 🗂️-----------------*", "yellow"))
    url = input("\n    Paste a URL containing Base64-encoded segments: ").strip()
    log(f"\n[INPUT_SPLIT_REPLACE] User input for Base64URLSplitter: {url}")

    base64Parts = SplitURL(url)

    if base64Parts:
        choice = input("   🛠️ Do you want to swap new Base64 into the URL (y/n): ").strip().lower()
        if choice == "y":
            URLReplace(base64Parts, url)

    print(colored("\n    *----------------------------------------------------------------------*", "yellow"))