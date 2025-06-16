"""
Name:
    ExitMain
Author:
    William Walker @ Crutchfield
Description:
        Handles  shutdown of WalkerTATools. Prompts the user to save
    or discard the session log before exiting. Ensures that logs are written
    to the appropriate directory or securely removed, maintaining workflow
    integrity without leaving behind unintended data.
imports:
    @WalkerLog.py
    termcolor   ---> For colored console output
"""
from termcolor import colored
from WalkerLog import *

def ExitMain():
    print(colored("\n    *---------------------------🧮 EXIT POINT 🧮---------------------------*", "red"))
    choice = input(colored("\n    📋 Would you like to save this session log? (y/n): ", "yellow")).strip().lower()
    log("\n[EXIT] User Exited The Program")

    if choice == "y":
        saved_path = WalkerLogSave()
        print(colored(f"\n    💾 Log saved to: {saved_path}", "green"))
    else:
        WalkerLogExit()
        print(colored("\n    🗑️ Session log discarded.", "red"))

    print(colored("\n    👋 Exiting WalkerTATools. Goodbye!\n", "red"))

    print(colored("\n    *----------------------------------------------------------------------*\n", "red"))
