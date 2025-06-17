
"""
Name:
    GLOBALS
Author:
    William Walker @ Crutchfield

Description:
        Contains Global Variables
"""
import os

"""GLOBALS FOR ENTIRE PROGRAM"""
RCHAINLIST = []

def MakeWalkerToolsFolder():
    documents_folder = os.path.join(os.path.expanduser("~"), "Documents")
    tools_root = os.path.join(documents_folder, "WalkerTATools")

    os.makedirs(tools_root, exist_ok=True)

    return tools_root