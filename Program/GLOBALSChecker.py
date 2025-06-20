"""
Name:
   GlobalChecker
Author:
    William Walker @ Crutchfield
Description:
             Checks the Acquired Globals to see if User is ready for
        Excel Exports with Guided input.

Imports:
     @GLOBALS.py
     termcolor --- For colored console output
"""
from termcolor import colored, cprint
import GLOBALS

def GlobalCheckerMain():
    cprint("\n              =--------[🔎 MISP SHEET CHECKER STATUS]--------=", "cyan", attrs=["bold"])

    checklist = [
        ("Addr", GLOBALS.SENDER_ADDRESS, True),
        ("Subj", GLOBALS.SENDER_SUBJECT, True),
        ("IP", GLOBALS.SENDER_IP, True),
        ("Name", GLOBALS.SENDER_DISPLAY, True),
        ("Files", GLOBALS.FILES, False),
        ("URL", GLOBALS.MAL_URL, True),
        ("Post", GLOBALS.POST_URL, False),
        ("Redirects", GLOBALS.RCHAINLIST, False),
        ("Links", GLOBALS.RESEARCH_LINKS, False)
    ]

    status_output = []
    ready = True

    for label, value, required in checklist:
        filled = bool(value)
        if filled:
            color = "green"
            tag = f"✓ {label}"
        elif required:
            color = "red"
            tag = f"X {label}"
            ready = False
        else:
            color = "blue"
            tag = f"• {label}"

        status_output.append(colored(f"[{tag}]", color))

    midpoint = len(status_output) // 2
    line1 = "                     " + " ".join(status_output[:midpoint])
    line2 = "             " + " ".join(status_output[midpoint:])

    print(line1)
    print(line2)

    if ready:
        cprint("                          Ready for Guided Excel Mode ✔️", "green", attrs=["bold"])
    else:
        cprint("                          Missing required fields ❌", "red", attrs=["bold"])
