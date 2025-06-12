"""
Name:
    SanitizeURL
Author:
    William Walker @ Crutchfield
Description:
            Provides functionality to sanitize URLs by working around characters
    such as '.' and 't' so that links are no longer clickable or
    accidentally visited. Useful for safely displaying potentially
    malicious or sensitive URLs in logs, reports, or analysis.

imports:
    pyperclip ---> For clipboard manipulation
    termcolor ---> For colored text
"""
import pyperclip
from termcolor import colored


def sanitize_http(url):
    if url.startswith("https://"):
        return url.replace("https://", "hxxps://", 1)
    elif url.startswith("http://"):
        return url.replace("http://", "hxxp://", 1)
    return url

def bracket_dots(url):
    return url.replace(".", "[.]")

def SanitizeURLMain():
    url = input("\n    Paste a URL to sanitize: ").strip()

    sanitizedHttp = sanitize_http(url)

    sanitizedHttpandBrackets = bracket_dots(sanitizedHttp)

    print(colored(f"\n    🔒 Sanitized URL: {sanitizedHttpandBrackets}", "green"))

    pyperclip.copy(sanitizedHttpandBrackets)

    print(colored("    📋 Sanitized URL copied to clipboard\n", "green"))