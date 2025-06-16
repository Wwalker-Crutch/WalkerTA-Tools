"""
Name:
    Base64Encode
Author:
    William Walker @ Crutchfield
Description:
    Executes encoding of plaintext strings into Base64 format.
    safely transmit or obscure
    text such as configuration data, credentials, or identifiers.

    This module prompts the user to input a string and returns the Base64-encoded result.
imports:
    @WalkerLog.py
    base64    ---> For Base64 encoding
    termcolor ---> For colored text
"""
from WalkerLog import *
import base64
from termcolor import colored

def EncodeBase64String(plain_text):
    try:
        encoded_bytes = base64.b64encode(plain_text.encode('utf-8'))
        return encoded_bytes.decode('utf-8')
    except Exception as e:
        return f"❌ Encoding Error: {e}"

def Base64EncodeMain():
    print(colored("\n    *-------------------------📣 Base64 Encoder 📣-------------------------*", "cyan"))
    text = input("\n    Paste the string you want to encode: ").strip()
    log(f"\n[INPUT_ENCODE] User Input For Base64 Encode: {text}")

    encoded = EncodeBase64String(text)
    log(f"\n[ENCODE] User Text Base64 Encoded: {encoded}")

    if encoded.startswith("❌"):
        print(colored(f"\n    {encoded}\n", "red"))
    else:
        print(colored(f"\n    ✅ Encoded Output: {encoded}\n", "green"))

    print(colored("\n    *----------------------------------------------------------------------*", "cyan"))

