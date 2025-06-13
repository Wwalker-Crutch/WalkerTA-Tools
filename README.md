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

- **Base64 Encode (`64e`)**  
  Encodes standard UTF-8 plaintext into Base64 format. Useful for obscuring sensitive strings.

- **Base64 URL Splitter and Replacer (`64url`)**  
  Splits and decodes Base64-encoded segments found inside URLs, Optionally allows you to replace sensitive elements with safe placeholders (e.g., `YOUR_COMPANY`, `ANON_USER`).

- **Sanitize URL (`s`)**  
  Rewrites suspicious or dangerous URLs so they are no longer clickable. Converts `http` to `hxxp` and wraps dots (`.`) with brackets like `[.]`.

- **Clear Terminal (`clr`)**  
  Clears the terminal screen and redisplays the CLI banner.

- **Exit (`eX`)**  
  Quits the CLI. Prompts for save or discard of a session log of your time working in WalkerTATools

---

### 🛠️ Usage:

Run `walkerTAtools.py` to start the tool:
python walkerTAtools.py

Once running, you'll be prompted to enter a command. Supported commands include:

64d      → Run Base64 Decode

64e      → Run Base64 Encode

64url    → Run Base64 URL Splitter and Replacer

s        → Sanitize a potentially dangerous URL

clr      → Clear the terminal

eX       → Exit the program

Each command routes to its respective logic via the central CLI engine.

---


### 📝 Session Logging

Each time you use WalkerTATools, a temporary session log is generated to record your actions, tool inputs, and outputs.

When you exit the program using the `eX` command, you’ll be prompted to either **save** or **discard** this session log.

If you choose to save it, WalkerTATools will create (or reuse) a folder called `WalkerTA_Logs` inside your **Documents** directory (e.g., `C:\Users\YourName\Documents\WalkerTA_Logs`). This folder will contain timestamped `.log` files documenting everything you did during that session.

This feature is great for:

- **Auditing** your triage workflow  
- **Referencing** past inputs and decoded results  
- **Sharing** logs with teammates for review or investigation  

If you discard the log, no trace of the session is saved—giving you full control over your workflow privacy.
