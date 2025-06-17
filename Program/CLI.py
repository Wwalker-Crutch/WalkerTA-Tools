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
    @base64URLSplitter.py
    @SanitizeURL.py
    @Base64Encode.py
    @Exit.py
    @Redirect.py
    @WalkerLog.py
    @ExcelHandler.py
    termcolor ---> For colored text
    os -----> to clear and do regular windows commands
"""
from Base64Decode import Base64DecodeMain
from Base64URLSplitter import Base64URLSplitterMain
from Redirect import RedirectMain
from SanitizeURL import SanitizeURLMain
from Base64Encode import Base64EncodeMain
from WalkerLog import *
from Exit import ExitMain
from termcolor import colored
from ExcelHandler import ExcelHandlerMain
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
    print("64url: Run Base64 URL Splitter and Replacer")
    print("eX:    Exit the program")
    print("clear: Clear the terminal")
    print("usage: Print the usage info")
    print("r:     Setup a Redirect")
    print("sheet: Setup a excel sheet with info from the program")
    print("-" * 55)

def PrintUsage():
    print("❌-------------------------------------------------❌")
    print(colored("            use one of these commands", "yellow"))
    print("s:       Sanitize a potentially dangerous URL")
    print("64d:     Command to run Base64 Decode")
    print("64e:     Command to run Base64 Encode")
    print("64url:   Command to run Base64 URL Splitter and Replacer")
    print("eX:      Exit the program")
    print("clear:   Clear the terminal")
    print("usage:   Print the usage info")
    print("r:       Setup a Redirect")
    print("sheet:   Setup a excel sheet with info from the program")
    print("❌-------------------------------------------------❌")

def PrintUsageError():
    print("❌-------------------------------------------------❌")
    print(colored("              Enter a valid command", "red"))
    print("s:       Sanitize a potentially dangerous URL")
    print("64d:     Command to run Base64 Decode")
    print("64e:     Command to run Base64 Encode")
    print("64url:   Command to run Base64 URL Splitter and Replacer")
    print("eX:      Exit the program")
    print("clear:   Clear the terminal")
    print("usage:   Print the usage info")
    print("r:       Setup a Redirect")
    print("sheet:   Setup a excel sheet with info from the program")
    print("❌-------------------------------------------------❌")

def ClearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def PreProcessing():
    tools_root = MakeWalkerToolsFolder()
    log(f"[TOOLS_FOLDER] Created (or confirmed) root tools folder at: {tools_root}")



    return


def CommandLineMain():
    PrettyPrint()
    log(f"\n[START]")

    PreProcessing()

    while True:
        flag = input("\nEnter Command: ").strip()
        log(f"\n[USER] Entered Command: {flag}")

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
        elif flag == "r":
            RedirectMain()
        elif flag == "sheet":
            ExcelHandlerMain()
        elif flag == "eX":
            ExitMain()
            break
        else:
            PrintUsageError()
