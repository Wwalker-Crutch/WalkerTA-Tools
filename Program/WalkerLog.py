"""
Name:
    WalkerLog
Author:
    William Walker @ Crutchfield
Description:
    Provides logging functionality for all WalkerTATools modules.
    This module captures user inputs, tool activity, and session events into
    a temporary log file. Logs are preserved only if explicitly saved.

    Key Features:
    - `log(message)`: Log CLI actions or tool-specific data
    - `Walker_log_save()`: Renames and moves the session log to a permanent folder
    - `walker_log_exit()`: Deletes the session log unless the user chooses to save
    - `make_walker_folder()`: Ensures all saved logs are organized in the user’s Documents/WalkerTA_Logs folder
Imports:
    logging   ---> For capturing and formatting session logs
    os        ---> For filesystem operations
    datetime  ---> To generate unique timestamps for saved logs
"""
import logging
import os
from datetime import datetime

WALKER_LOG_FILE = "walker_temp.log"

logger = logging.getLogger("walker_logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(WALKER_LOG_FILE, mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(message)s", "%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def log(message):
    logger.info(message)

def make_walker_folder():
    documents_folder = os.path.join(os.path.expanduser("~"), "Documents")
    logs_folder = os.path.join(documents_folder, "WalkerTA_Logs")
    os.makedirs(logs_folder, exist_ok=True)
    return logs_folder

def Walker_log_save():
    logs_folder = make_walker_folder()

    logger.removeHandler(file_handler)
    file_handler.close()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"walker_session_{timestamp}.log"
    full_path = os.path.join(logs_folder, filename)

    os.rename(WALKER_LOG_FILE, full_path)
    return full_path

def walker_log_exit():
    logger.removeHandler(file_handler)
    file_handler.close()
    if os.path.exists(WALKER_LOG_FILE):
        os.remove(WALKER_LOG_FILE)



