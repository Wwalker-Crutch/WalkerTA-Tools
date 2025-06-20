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
    @EmailSpecs.py
    @DeSanitizeURL.py
    termcolor ---> For colored text
    os -----> to clear and do regular windows commands
"""
from Base64Decode import Base64DecodeMain
from Base64URLSplitter import Base64URLSplitterMain
from Redirect import RedirectMain
from SanitizeURL import SanitizeURLMain
from Base64Encode import Base64EncodeMain
from SHA256Sum import SHA256SumMain
from WalkerLog import *
from Exit import ExitMain
from termcolor import colored
from ExcelHandler import ExcelHandlerMain
from EmailDump import EmailDumpMain
from FileDump import FileDumpMain
from URLDump import URLDumpMain
from IPDump import IPDumpMain
from DeSanitizeURL import DesanitizeURLMain
import os


def PrettyPrint():
    print("\n      " + "*" * 65)
    print(colored("              🛠️  Welcome to WalkerTATools CLI Edition  🛠️", "yellow"))
    print(colored("                 Created by William Walker, @ Crutchfield", "yellow"))
    print("      "+"*" * 65)
    print(colored("-" * 85, "yellow"))
    print(colored("                   🧰  Usage Guide for WalkerTATools  🧰", "yellow"))
    print()
    print(colored("     *--------------------🧨 SINGLE USE COMMANDS 🧨----------------------*", "blue"))
    print("         s:        Sanitize a potentially dangerous URL")
    print("         ds:       Desanitize a URL for investigation")
    print("         64d:      Run Base64 Decode")
    print("         64e:      Command to run Base64 Encode")
    print("         256:      Run SHA256Sum on a File or Plaintext, Creates Hash")
    print("         64url:    Run Base64 URL Splitter and Replacer")
    print("         r:        Setup a Redirect")
    print()
    print(colored("     *-------------------------🎯 REPORTING 🎯---------------------------*", "blue"))
    print("         ed:       Email Paster and Collector")
    print("         fd:       File Paster and Collector")
    print("         ud:       URL Paster and Collector")
    print("         id:       IP Paster and Collector")
    print("         sheet:    Setup an Excel sheet with info from the program, EML, or manual")
    print()
    print(colored("     *----------------------💻 PROGRAM COMMANDS 💻-----------------------*", "blue"))
    print("         eX:       Exit the program")
    print("         clear:    Clear the terminal")
    print("         usage:    Print the usage info")
    print()

    print(colored("-" * 85, "yellow"))

def PrintUsage():
    print(colored("\n*" + "-" * 88 + "*", "blue"))
    print(colored("                   📘  Usage Help for WalkerTATools  📘", "yellow"))
    print()
    print(colored("     *--------------------🧨 SINGLE USE COMMANDS 🧨----------------------*", "blue"))
    print("         s:        Sanitize a potentially dangerous URL")
    print("         ds:       Desanitize a URL for investigation")
    print("         64d:      Run Base64 Decode")
    print("         64e:      Command to run Base64 Encode")
    print("         256:      Run SHA256Sum on a File or Plaintext, Creates Hash")
    print("         64url:    Run Base64 URL Splitter and Replacer")
    print("         r:        Setup a Redirect")
    print()
    print(colored("     *-------------------------🎯 REPORTING 🎯---------------------------*", "blue"))
    print("         ed:       Email Paster and Collector")
    print("         fd:       File Paster and Collector")
    print("         ud:       URL Paster and Collector")
    print("         id:       IP Paster and Collector")
    print("         sheet:    Setup an Excel sheet with info from the program, EML, or manual")
    print()
    print(colored("     *----------------------💻 PROGRAM COMMANDS 💻-----------------------*", "blue"))
    print("         eX:       Exit the program")
    print("         clear:    Clear the terminal")
    print("         usage:    Print the usage info")
    print()
    print(colored("\n*" + "-" * 88 + "*", "blue"))


def PrintUsageError():
    print(colored("\n*" + "-" * 88 + "*", "red"))
    print(colored("                ❌  Invalid Command — Please Try Again  ❌", "red"))
    print()
    print(colored("     *--------------------🧨 SINGLE USE COMMANDS 🧨----------------------*", "blue"))
    print("         s:        Sanitize a potentially dangerous URL")
    print("         ds:       Desanitize a URL for investigation")
    print("         64d:      Run Base64 Decode")
    print("         64e:      Command to run Base64 Encode")
    print("         256:      Run SHA256Sum on a File or Plaintext, Creates Hash")
    print("         64url:    Run Base64 URL Splitter and Replacer")
    print("         r:        Setup a Redirect")
    print()
    print(colored("     *-------------------------🎯 REPORTING 🎯---------------------------*", "blue"))
    print("         ed:       Email Paster and Collector")
    print("         fd:       File Paster and Collector")
    print("         ud:       URL Paster and Collector")
    print("         id:       IP Paster and Collector")
    print("         sheet:    Setup an Excel sheet with info from the program, EML, or manual")
    print()
    print(colored("     *----------------------💻 PROGRAM COMMANDS 💻-----------------------*", "blue"))
    print("         eX:       Exit the program")
    print("         clear:    Clear the terminal")
    print("         usage:    Print the usage info")
    print()
    print(colored("\n*" + "-" * 88 + "*", "red"))


def ClearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def PreProcessing():
    tools_root = MakeWalkerToolsFolder()
    log(f"\n[TOOLS_FOLDER] Created (or confirmed) root tools folder at: {tools_root}")

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
        elif flag == "ds":
            DesanitizeURLMain()
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
        elif flag == "256":
            SHA256SumMain()
        elif flag == "ed":
            EmailDumpMain()
        elif flag == "fd":
            FileDumpMain()
        elif flag == "ud":
            URLDumpMain()
        elif flag == "id":
            IPDumpMain()
        elif flag == "eX":
            if ExitMain():
                break
        else:
            PrintUsageError()



