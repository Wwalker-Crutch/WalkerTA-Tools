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
    @SanitizeURL.py
    @Base64Encode.py
    @Exit.py
    @WalkerLog.py
    termcolor ---> For colored text
    os -----> to clear and do regular windows commands
"""
from Base64Decode import Base64DecodeMain
from Base64URLSplitter import Base64URLSplitterMain
from SanitizeURL import SanitizeURLMain
from Base64Encode import Base64EncodeMain
from WalkerLog import *
from Exit import ExitMain
from termcolor import colored
import os


def PrettyPrint():
    print("\n" + "*" * 53)
    print(colored("   🛠️  Welcome to WalkerTATools — CLI Edition  🛠️ ", "yellow"))
    print(colored("       Created by William Walker @ Crutchfield", "yellow"))
    print("*" * 53)
    print("-" * 55)
    print(colored("       🧰  Usage Guide for WalkerTATools  🧰", "yellow"))
    print("s:     Sanitize a potentially dangerous URL")
    print("64d:   Run Base64 Decode")
    print("64e:   Command to run Base64 Encode")
    print("64url: Run Base64 URL Splitter")
    print("eX:    Exit the program")
    print("clear: Clear the terminal")
    print("usage: Print the usage info")
    print("-" * 55)

def PrintUsage():
    print("❌-------------------------------------------------❌")
    print(colored("            use one of these commands", "yellow"))
    print("s:       Sanitize a potentially dangerous URL")
    print("64d:     Command to run Base64 Decode")
    print("64e:     Command to run Base64 Encode")
    print("64url:   Command to run Base64 URL Splitter")
    print("eX:      Exit the program")
    print("clear:   Clear the terminal")
    print("usage:   Print the usage info")
    print("❌-------------------------------------------------❌")

def PrintUsageError():
    print("❌-------------------------------------------------❌")
    print(colored("              Enter a valid command", "red"))
    print("s:       Sanitize a potentially dangerous URL")
    print("64d:     Command to run Base64 Decode")
    print("64e:     Command to run Base64 Encode")
    print("64url:   Command to run Base64 URL Splitter")
    print("eX:      Exit the program")
    print("clear:   Clear the terminal")
    print("usage:   Print the usage info")
    print("❌-------------------------------------------------❌")

def ClearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def CommandLineMain():
    PrettyPrint()

    while True:
        flag = input("Enter Command: ").strip()
        log(f"Entered Command: {flag}")

        if flag == "64d":
            Base64DecodeMain()
        elif flag == "64e":
            Base64EncodeMain()
        elif flag == "s":
            SanitizeURLMain()
        elif flag == "64url":
            Base64URLSplitterMain()
        elif flag == "clear":
            ClearTerminal()
        elif flag == "usage":
            PrintUsage()
        elif flag == "eX":
            ExitMain()
            break
        else:
            PrintUsageError()
