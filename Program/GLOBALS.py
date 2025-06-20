
"""
Name:
    GLOBALS
Author:
    William Walker @ Crutchfield

Description:
        Contains Global Variables and various Global Functions
"""
import os

"""GLOBALS FOR ENTIRE PROGRAM"""
RCHAINLIST = []
WALKER_LOG_FILE = "walker_temp.log"
SENDER_ADDRESS = ""
FOUND_EMAILS = []
FILES = []
SENDER_RETURN_PATH = ""
SENDER_FROM = ""
URL_LIST = []
MAL_URL = ""
POST_URL = ""
SENDER_IP = ""
IP_LIST = {}
RESEARCH_LINKS = []
SENDER_SUBJECT = ""
SENDER_DISPLAY = ""


def MakeWalkerToolsFolder():
    documents_folder = os.path.join(os.path.expanduser("~"), "Documents")
    tools_root = os.path.join(documents_folder, "WalkerTATools")

    os.makedirs(tools_root, exist_ok=True)
    return tools_root