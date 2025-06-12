# 🧰 WalkerTATools, CLI Triage and Analysis Utlity Program

### Author:
William Walker @ Crutchfield

---

### 📦 Description:
WalkerTATools is a modular command-line toolkit built to assist in decoding, parsing, and safely presenting potentially dangerous strings and URLs during research, analysis, and triage workflow

---

### 🚀 Features:

- **Base64 Decode (`64d`)**  
  Decodes standard Base64-encoded strings for analysis or cleanup. Accepts both padded and unpadded input.

- **Base64 URL Splitter (`64url`)**  
  Splits and decodes Base64-encoded segments found inside URLs, replacing sensitive elements with safe placeholders (e.g., `YOUR_COMPANY`, `ANON_USER`).

- **Sanitize URL (`s`)**  
  Rewrites suspicious or dangerous URLs so they are no longer clickable. Converts `http` to `hxxp` and wraps dots (`.`) with brackets like `[.]`.

- **Clear Terminal (`clr`)**  
  Clears the terminal screen and redisplays the CLI banner.

- **Exit (`eX`)**  
  Gracefully quits the CLI.

---

### 🛠️ Usage:

Run `walkerTAtools.py` to start the tool:
python walkerTAtools.py

Once running, you'll be prompted to enter a command. Supported commands include:

64d      → Run Base64 Decode

64url    → Run Base64 URL Splitter

s        → Sanitize a potentially dangerous URL

clr      → Clear the terminal

eX       → Exit the program

Each command routes to its respective logic via the central CLI engine.
