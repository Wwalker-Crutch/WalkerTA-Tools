"""
Name:
    Base64Decode
Author:
    William Walker @ Crutchfield
Description:
        Executes decoding for standard Base64-encoded input. Designed for
    use cases where users encounter Base64 strings in URLs or obfuscated content.

        This command allows users to paste any Base64 string and receive
    the decoded output, making it easier to analyze encoded data.

imports:
    @WalkerLog.py
    base64    ---> For Base64 decoding
    termcolor ---> For colored text
"""
import base64
from termcolor import colored
from WalkerLog import *

def DecodeBase64String(b64_string):
    try:
        decoded = base64.b64decode(b64_string)
        return decoded.decode('utf-8')
    except Exception as e:
        return f"❌ Decoding Error: {e}"


def Base64DecodeMain():
    print(colored("\n    *-------------------------🧭 Base64 Decoder 🧭-------------------------*", "blue"))
    b64 = input("\n    Paste your Base64-encoded string: ").strip()
    log(f"\n[INPUT_DECODE] User Input For Base64 Decode: {b64}")

    decoded = DecodeBase64String(b64)
    log(f"\n[DECODE] Decoded Base64 String: {decoded}")

    if decoded.startswith("❌"):
        print(colored(f"\n    {decoded}\n", "red"))
    else:
        print(colored(f"\n    ✅ Decoded Output: {decoded}\n", "green"))

    print(colored("\n    *----------------------------------------------------------------------*", "blue"))
