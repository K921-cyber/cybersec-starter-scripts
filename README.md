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
