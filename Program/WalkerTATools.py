"""
Name:
    WalkerTATools ( main )
Author:
    William Walker @ Crutchfield
Description:
        Entry point for WalkerTATools. While this script functions
    as the main launcher, it delegates workflow to the Command Line Interface
    defined in CLI.py, providing a user-friendly interface for executing
    supported decoding tools.

imports:
    @ClI.py

"""
from CLI import CommandLineMain


if __name__ == "__main__":
    CommandLineMain()
