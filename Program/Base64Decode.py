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
    base64    ---> For Base64 decoding
    termcolor ---> For colored text
"""
import base64
from termcolor import colored

def decode_base64_string(b64_string):
    try:
        decoded = base64.b64decode(b64_string)
        return decoded.decode('utf-8')
    except Exception as e:
        return f"❌ Decoding Error: {e}"


def Base64DecodeMain():
    b64 = input("\n    Paste your Base64-encoded string: ").strip()

    decoded = decode_base64_string(b64)

    if decoded.startswith("❌"):
        print(colored(f"\n    {decoded}\n", "red"))
    else:
        print(colored(f"\n    ✅ Decoded Output: {decoded}\n", "green"))
