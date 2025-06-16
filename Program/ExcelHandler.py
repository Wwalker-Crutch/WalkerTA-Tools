"""
Name:
    ExitMain
Author:
    William Walker @ Crutchfield
Description:

imports:
    @WalkerLog.py
    termcolor   ---> For colored console output
"""
from WalkerLog import *
from termcolor import colored

def GuidedExcelLogging():
    return

def ManualExcelLogging():
    return




def ExcelHandlerMain():
    print(colored("\n    *-------------------------📶 Excel Logging 📶--------------------------*", "magenta"))

    mode = input("\n    Choose logging mode, Guided or Manual (g/m): ").strip().lower()

    if mode == "g":
        GuidedExcelLogging()
    elif mode == "m":
        ManualExcelLogging()
    else:
        print(colored("    ❌ Invalid option. Please choose 'G' or 'M'.", "red"))

    print(colored("\n    *----------------------------------------------------------------------*", "magenta"))