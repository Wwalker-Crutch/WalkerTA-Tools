"""
Name:
    CLI ( Command Line Interface )
Author:
    William Walker @ Crutchfield
Description:
        CLI.py provides a text-based interface for interacting
    with various utilities. It routes user input to specific
    processing functions and manages all console-based messaging.

imports:
    @base64Decode.py
    @base64URLSplitterMain.py
"""
from Base64Decode import Base64DecodeMain
from Base64URLSplitter import Base64URLSplitterMain
from SanitizeURL import SanitizeURLMain


def PrettyPrint():
    print("\n" + "*" * 53)
    print("   🛠️  Welcome to WalkerTATools — CLI Edition  🛠️ ")
    print("       Created by William Walker @ Crutchfield")
    print("*" * 53)
    print("-" * 55)
    print("       🧰  Usage Guide for WalkerTATools  🧰")
    print("  s:     Sanitize a potentially dangerous URL")
    print("  64:    Run Base64 Decode")
    print("  64url: Run Base64 URL Splitter")
    print("  eX:     Exit the program")
    print("-" * 55)

def PrintUsageError():
    print("❌-------------------------------------------------❌")
    print("Usage:   Enter a valid command ")
    print("s:       Sanitize a potentially dangerous URL")
    print("64:      Command to run Base64 Decode")
    print("64url:   Command to run Base64 URL Splitter")
    print("ex:       Exit the program")
    print("❌-------------------------------------------------❌")

def CommandLineMain():
    PrettyPrint()

    while True:
        flag = input("Enter Command: ").strip()

        if flag == "64":
            Base64DecodeMain()
        elif flag == "s":
            SanitizeURLMain()
        elif flag == "64url":
            Base64URLSplitterMain()
        elif flag == "eX":
            print("\n👋 Exiting WalkerTATools. Goodbye!\n")
            break
        else:
            PrintUsageError()
