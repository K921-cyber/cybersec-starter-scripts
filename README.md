# 🔐 CyberSec Starter Scripts — Python Edition

> 🎓 Beginner-friendly cybersecurity scripts to learn core concepts: hashing, scanning, integrity monitoring, and password strength evaluation.  
> ⚠️ Educational use only — never test on systems without permission.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Beginner Friendly](https://img.shields.io/badge/Difficulty-Beginner-brightgreen)

---

## 🧰 What’s Included?

| Script | Purpose | Why It Matters |
|--------|---------|----------------|
| `password_strength.py` | Checks if a password is strong (length, digits, symbols, etc.) | Learn how attackers evaluate weak passwords |
| `hash_generator.py` | Generates SHA-256 or MD5 hashes from input text or files | Understand how passwords/data are stored securely (or not!) |
| `port_scanner.py` | Scans top 10 ports on a target IP (TCP connect scan) | Learn basics of network reconnaissance |
| `file_integrity_checker.py` | Compares file hash over time to detect tampering | Core concept in malware detection & system monitoring |
| `banner_grabber.py` | Retrieves service version information from open ports | Helps fingerprint services for vulnerabilities |

📁 All scripts are standalone — no complex setup needed.

---

## 🧩 Concept Flow (How All Scripts Work Together)

```mermaid
flowchart LR
    A[User] --> B[password_strength.py]
    A --> C[hash_generator.py]
    A --> D[port_scanner.py]
    A --> E[file_integrity_checker.py]
    A --> F[banner_grabber.py]

    B --> B1[Check Password Strength]
    C --> C1[Generate Hash from Text/File]
    E --> E1[Verify File Integrity via Hash Comparison]

    D --> D1[Scan for Open Ports]
    D1 --> F
    F --> F1[Fetch Service Banner & Version]

    C1 --> E
```
# ⚙️ Installation & Setup

You only need **Python 3.8+** — no external libraries required.

```bash
git clone https://github.com/K921-cyber/cybersec-starter-scripts.git
cd cybersec-starter-scripts
```
# 📘 Detailed Script Documentation

---

## 1️⃣ `password_strength.py` — Password Strength Checker

Evaluates the strength of a password based on:

- Length  
- Digits  
- Symbols  
- Uppercase and lowercase characters  

### Flowchart

```mermaid
flowchart TD
    A[Enter Password] --> B[Check Length]
    B --> C[Check Uppercase Characters]
    C --> D[Check Lowercase Characters]
    D --> E[Check Digits]
    E --> F[Check Symbols]
    F --> G[Calculate Strength Score]
    G --> H[Output: Weak / Medium / Strong]

```
## 2️⃣ `hash_generator.py` — Hash Generator

Generates secure hashes (SHA-256 or MD5) from:

- Input text  
- File contents  

### Flowchart
```mermaid
flowchart TD
    A[Select Mode: Text / File] --> B[Choose Hash Algorithm]
    B --> C{Text Mode?}
    C --> |Yes| D[Input Text → Generate Hash]
    C --> |No| E[Choose File → Read File → Generate Hash]
    D --> F[Display Hash Output]
    E --> F
```

## 3️⃣ port_scanner.py — Basic Port Scanner

Performs a TCP connect scan on the 10 most common ports.

Flowchart
```mermaid
flowchart TD
    A[Enter Target IP / Hostname] --> B[Load Top 10 Ports]
    B --> C[Attempt TCP Connection on Each Port]
    C --> D{Connection Successful?}
    D --> |Yes| E[Port is OPEN]
    D --> |No| F[Port is CLOSED or REFUSED]
    E --> G[Add to Results]
    F --> G
    G --> H[Display Scan Results]
```
## 4️⃣ file_integrity_checker.py — File Integrity Checker

Detects file tampering by comparing current and baseline hashes.

Flowchart
```mermaid
flowchart TD
    A[Enter File Path] --> B{Baseline Hash Exists?}
    B --> |No| C[Generate & Save Baseline Hash]
    B --> |Yes| D[Generate New Hash]
    D --> E{Hashes Match?}
    E --> |Yes| F[File is Untouched]
    E --> |No| G[WARNING: File Modified]
```

## 5️⃣ banner_grabber.py — Banner Grabber

Retrieves service banner/version information from an open port.

Flowchart
```mermaid
flowchart TD
    A[Enter Host & Port] --> B[Open TCP Socket]
    B --> C[Send Request or Wait for Banner]
    C --> D{Banner Received?}
    D --> |Yes| E[Display Banner Data]
    D --> |No| F[No Response or Service Hidden]
```
# 📄 License

This project is licensed under the MIT License.
You may use, modify, and distribute this project responsibly.




