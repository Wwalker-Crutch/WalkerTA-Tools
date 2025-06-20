# 🧰 WalkerTATools, CLI Triage and Analysis Utlity Program

### Author:
William Walker @ Crutchfield

---

### 📦 Description

**WalkerTATools** is a modular command-line triage and analysis utility engineered to streamline and strengthen security workflows, from initial threat assessment all the way to structured MISP reporting. Built with both flexibility and clarity in mind, this toolkit empowers analysts, researchers, and SOC operators to quickly extract, decode, sanitize, and organize key indicators of compromise (IOCs) during real-time investigations or retrospective reporting.

It brings together a set of focused tools designed to handle:

- 🧨 **Single-use analysis tasks** like Base64 decoding/encoding, SHA256 hashing, and advanced URL sanitization 
- 🛡️ **Malware triage workflows**, including safe decoding and redaction of suspicious payloads embedded in URLs or files  
- 📬 **Email, file, and URL IOC collection** with structured prompts that prepare entries for direct injection into MISP or intelligence reports.
- 📊 **Session logging** to provide a tamper-free audit trail of analyst actions, choices, and findings  
- 📁 **Export-ready Excel sheet creation** from collected artifacts, reducing the manual prep time needed to convert findings into reportable formats. WalkerTATools will tell you how close you are to completing a MISP report after certain commands. 

**WalkerTATools** acts as your CLI-sidekick, guiding you through evidence processing and helping ensure every string, email, URL, and file hash is accounted for, safely documented, and MISP-ready.

---
### 🧩 Feature Categories:

#### *🧨 SINGLE USE COMMANDS*
- **Sanitize URL (`s`)**  
  Rewrites suspicious or dangerous URLs so they are no longer clickable. Converts `http` to `hxxp` and wraps dots (`.`) with brackets like `[.]`.

- **Desanitize URL (`ds`)**  
  Reverts sanitized URLs back to their original form. Converts hxxp to http and replaces bracketed dots like `[.]` with regular dots (`.`), restoring the clickable format for analysis or submission.

- **Base64 Decode (`64d`)**  
  Decodes standard Base64-encoded strings for analysis or cleanup. Accepts both padded and unpadded input.

- **Base64 Encode (`64e`)**  
  Encodes standard UTF-8 plaintext into Base64 format. Useful for obscuring sensitive strings.

- **SHA256SUM (`256`)**  
  Hashes a file or Plaintext using SHA256 checksum.

- **Base64 URL Splitter and Replacer (`64url`)**  
  Splits and decodes Base64-encoded segments found inside URLs. Optionally allows you to replace sensitive elements with safe placeholders (e.g., `YOUR_COMPANY`, `ANON_USER`).

#### *🎯 REPORTING*
- **Email Dump (`ed`)**  
  Collect and dedicate emails toward being a sender. Place for email collection. Used later in MISP report sheet guided mode.

- **File Dump (`fd`)**  
  Collect file names and associated SHA256 hashes for IOC reference and export. Used later in MISP report sheet guided mode.

- **URL Dump (`ud`)**  
  Collect and sanitize various malicious and credential-harvesting URLs for MISP-ready formatting. Used later in MISP report sheet guided mode.

- **IP Dump (`id`)**  
  Collect and label IP addresses associated with suspicious senders, indicators, or websites. Used later in MISP report sheet guided mode.

- **Redirect Chaining (`r`)**  
  Build and manage redirect chains using sanitized URLs. Create new chains or extend existing ones while keeping links safe and non-clickable for secure analysis and documentation. Used Later in MISP report sheet guided mode. 

- **Excel Sheet Builder (`sheet`)**  
  Build MISP-ready Excel sheets using collected IOCs and metadata for report output.

#### *💻 PROGRAM COMMANDS*
- **Clear Terminal (`clear`)**  
  Clears the terminal screen and redisplays the CLI banner.

- **Usage Menu (`usage`)**  
  Prints the usage of WalkerTATools.

- **Exit (`eX`)**  
  Quits the CLI. Prompts to save or discard the session log of your work.

- **Global Print (`G`)**  
  Prints Your current stored variables from the work You have done already. 

---

### 🛠️ Usage:

Run the tool from terminal in the WalkerTATools program folder with:
python walkerTAtools.py

#### *🧨 SINGLE USE COMMANDS*
- `s`   → Sanitize a potentially dangerous URL
- `ds`   → Desanitize a URL to investigate
- `64d`  → Base64 Decode  
- `64e`  → Base64 Encode  
- `256`  → SHA256 hash for file or plaintext  
- `64url` → Decode & redact Base64 strings in URLs  

#### *🎯 MISP REPORTING*
- `ed`  → Email Paster and Collector  
- `fd`  → File Paster and Collector  
- `ud`  → URL Paster and Collector
- `id`  → IP Paster and Collector
- `r`   → Create/edit sanitized redirect chains
- `sheet` → Build MISP-ready Excel sheet from collected data  

#### *💻 PROGRAM COMMANDS*
- `eX`  → Exit WalkerTATools, with save/discard log option  
- `clear` → Clear terminal output  
- `usage` → Print the usage menu
- `G`     → Print stored variables

Each command routes to its respective logic via the central CLI engine.

---

<sub>Contact: For questions and inquiries contact me at wbw1991@g.rit.edu</sub>
