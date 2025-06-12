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
    termcolor ---> For colored text
    os -----> to clear and do regular windows commands
"""
from Base64Decode import Base64DecodeMain
from Base64URLSplitter import Base64URLSplitterMain
from SanitizeURL import SanitizeURLMain
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
    print("64:    Run Base64 Decode")
    print("64url: Run Base64 URL Splitter")
    print("eX:    Exit the program")
    print("clear:   Clear the terminal")
    print("-" * 55)

def PrintUsageError():
    print("❌-------------------------------------------------❌")
    print(colored("              Enter a valid command", "red"))
    print("s:       Sanitize a potentially dangerous URL")
    print("64:      Command to run Base64 Decode")
    print("64url:   Command to run Base64 URL Splitter")
    print("eX:      Exit the program")
    print("clear:     Clear the terminal")
    print("❌-------------------------------------------------❌")

def ClearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

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
        elif flag == "clear":
            ClearTerminal()
        elif flag == "eX":
            print(colored("\n    👋 Exiting WalkerTATools. Goodbye!\n", "red"))
            break
        else:
            PrintUsageError()
