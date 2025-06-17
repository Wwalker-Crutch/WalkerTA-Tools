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
from GLOBALS import *
import os

def MakeWalkerExcelFolder():
    walker_root = MakeWalkerToolsFolder()

    excel_folder = os.path.join(walker_root, "WalkerTAExcel")
    os.makedirs(excel_folder, exist_ok=True)

    log(f"[EXCEL_FOLDER] Created (or confirmed) Excel folder at: {excel_folder}")
    return excel_folder


def GuidedExcelLogging():
    folder = MakeWalkerExcelFolder()



    return

def ManualExcelLogging():
    folder = MakeWalkerExcelFolder()



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