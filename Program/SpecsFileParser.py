"""
Name:
    EmailSpecs
Author:
    William Walker @ Crutchfield
Description:
    Handles collection of email specifications via guided input or from file.

Imports:
    @WalkerLog.py
    @GLOBALS.py
    termcolor --- For colored console output
"""
from email import policy
from email.parser import BytesParser
import re
from termcolor import colored
import GLOBALS
from WalkerLog import *
from SanitizeURL import SanitizeURL
from SHA256Sum import SHA256FromString



def extract_urls(text):
    return re.findall(r"https?://[^\s'\"<>]+", text)



def HandleExtractedURLs(msg):
    if msg.is_multipart():
        parts = [part.get_content() for part in msg.walk() if part.get_content_type() == "text/plain"]
        body = "\n".join(parts)
    else:
        body = msg.get_content()

    urls = extract_urls(body)
    GLOBALS.URL_LIST = urls

    if urls:
        print(colored("\n    🌐 URLs found in email:", "yellow"))
        for i, u in enumerate(urls):
            print(f"     [{i}] {u}")
        choice = input("\n    ➤ Enter index of malicious URL (or press Enter to skip): ").strip()
        if choice.isdigit() and int(choice) < len(urls):
            GLOBALS.MAL_URL = SanitizeURL(urls[int(choice)])
            print(colored(f"\n    ✅ MAL_URL set to: {GLOBALS.MAL_URL}", "green"))
    else:
        print(colored("    ❌ No URLs found in message body.", "red"))


def HandleAttachments(msg):
    attachments = []
    for part in msg.iter_attachments():
        filename = part.get_filename()
        if filename:
            attachments.append(filename)

    if attachments:
        print(colored("\n    📎 Attachments found:", "yellow"))
        for i, name in enumerate(attachments):
            print(f"     [{i}] {name}")
        choice = input("\n    ➤ Enter index of filename to hash as string & include in FILES (or press Enter to skip): ").strip()
        if choice.isdigit() and int(choice) < len(attachments):
            name = attachments[int(choice)]
            hashed = SHA256FromString(name)
            if hashed:
                GLOBALS.FILES.append(hashed)
    else:
        print(colored("    ❌ No named attachments found.", "red"))



def extract_sender_ip(headers):

    # TODO: THIS DOESNT WORK FULLY FIX

    received_headers = headers.get_all("Received", [])
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    for header in reversed(received_headers):  # earliest Received at the bottom
        match = re.search(ip_pattern, header)
        if match:
            return match.group(0)
    return "(IP not found)"




def EmailSpecsFromFile(file_path):
    print(colored("\n    📧 Parsing EML file for header and body content...", "cyan"))

    try:
        with open(file_path, "rb") as f:
            msg = BytesParser(policy=policy.default).parse(f)

        GLOBALS.SENDER_ADDRESS = msg.get("From")
        GLOBALS.SENDER_SUBJECT = msg.get("Subject")
        GLOBALS.SENDER_DISPLAY = msg.get("From").split("<")[0].strip() if "<" in GLOBALS.SENDER_ADDRESS else GLOBALS.SENDER_ADDRESS
        GLOBALS.SENDER_IP = extract_sender_ip(msg)
        GLOBALS.SENDER_RETURN_PATH = msg.get("Return-Path")
        GLOBALS.SENDER_FROM = msg.get("Sender")

        HandleExtractedURLs(msg)
        HandleAttachments(msg)

        log(f"\n[EMAIL_SPECS_FROM_FILE] SENDER: {GLOBALS.SENDER_ADDRESS}")
        log(f"\n[EMAIL_SPECS_FROM_FILE] SUBJECT: {GLOBALS.SENDER_SUBJECT}")
        log(f"\n[EMAIL_SPECS_FROM_FILE] DISPLAY: {GLOBALS.SENDER_DISPLAY}")
        log(f"\n[EMAIL_SPECS_FROM_FILE] IP: {GLOBALS.SENDER_IP}")
        log(f"\n[EMAIL_SPECS_FROM_FILE] URLs: {GLOBALS.URL_LIST}")
        log(f"\n[EMAIL_SPECS_FROM_FILE] MAL_URL: {GLOBALS.MAL_URL}")
        log(f"\n[EMAIL_SPECS_FROM_FILE] FILES: {GLOBALS.FILES}")
        log(f"\n[EMAIL_SPECS_FROM_FILE] RETURN_PATH: {GLOBALS.SENDER_RETURN_PATH}")
        log(f"\n[EMAIL_SPECS_FROM_FILE] SENDER_FROM: {GLOBALS.SENDER_FROM}")

    except Exception as e:
        print(colored(f"    ❌ Failed to parse EML file: {e}", "red"))
