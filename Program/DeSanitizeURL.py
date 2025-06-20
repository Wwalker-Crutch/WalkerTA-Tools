"""
Name:
    DesanitizeURL
Author:
    William Walker @ Crutchfield
Description:
    Reverses the sanitization of URLs by converting obfuscated components
    such as 'hxxp' and '[.]' back to their original forms. This is useful
    for testing, analysis, or investigation purposes where the original
    URL format is required.

    ⚠️ WARNING: Desanitizing URLs can make them active and potentially dangerous.
    Use with caution and only in secure environments.

Imports:
    @WalkerLog.py
    termcolor --- For colored console output
    pyperclip --- Clipboard
"""

from WalkerLog import *
from termcolor import colored
import pyperclip

def DesanitizeURL(url):
    if not url:
        return ""

    desanitized = url.replace("hxxps://", "https://").replace("hxxp://", "http://").replace("[.]", ".")
    log(f"\n[DESAND] Desanitized URL: {desanitized}")
    return desanitized


def DesanitizeURLMain():
    print(colored("\n    *---------------------⚠️ Desanitization Zone ⚠️----------------------*", "red"))
    url = input("\n     Paste a sanitized URL to desanitize: ").strip()

    desanitized = DesanitizeURL(url)

    pyperclip.copy(desanitized)

    print(colored(f"\n    🔓 Desanitized URL: {desanitized}", "yellow"))
    print(colored("    ⚠️ WARNING: This URL is now active and may be dangerous. Handle with care!", "red", attrs=["bold"]))
    print(colored("    📋 Desanitized URL copied to clipboard", "red"))
    print(colored("\n    *----------------------------------------------------------------------*", "red"))
