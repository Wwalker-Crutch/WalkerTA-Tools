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
    choice = input(colored("\n    📋 Would you like to save this session log? (y/n): ", "yellow")).strip().lower()

    if choice == "y":
        saved_path = Walker_log_save()
        print(colored(f"\n    💾 Log saved to: {saved_path}", "green"))
    else:
        walker_log_exit()
        print(colored("\n    🗑️ Session log discarded.", "red"))

    print(colored("\n    👋 Exiting WalkerTATools. Goodbye!\n", "red"))
