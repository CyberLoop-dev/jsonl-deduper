<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:14b8a6&height=170&section=header&text=JSONL%20Deduper&fontColor=ffffff&fontSize=38&animation=fadeIn" width="100%" alt="JSONL Deduper banner"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&duration=2800&pause=900&color=14B8A6&center=true&vCenter=true&width=650&lines=Remove+duplicate+JSONL+records;Use+canonical+JSON+or+selected+keys;Keep+the+first+matching+record" alt="Typing introduction"/>
<p>Deduplicate JSON Lines files without changing the original.</p>
<p><img src="https://img.shields.io/github/license/CyberLoop-dev/jsonl-deduper?style=for-the-badge" alt="License"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/jsonl-deduper?style=for-the-badge" alt="Language"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/jsonl-deduper?style=for-the-badge" alt="Stars"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/jsonl-deduper?style=for-the-badge" alt="Last commit"/></p>
<img src="assets/icon.svg" width="112" alt="Project icon"/>
</div>

## ✨ Overview
JSONL Deduper reads newline-delimited JSON records, computes a stable comparison key, and writes only the first occurrence of each record to a new file. The input remains untouched.

## 🚀 Features
- ✨ Deduplicate by the full canonical JSON object
- ✨ Optionally compare only selected fields with repeated `--key` flags
- ✨ Preserve the first matching record and original field values
- ✨ Report duplicates and malformed line numbers
- ✨ Skip invalid lines only when explicitly requested

## 🎬 Demo
`python main.py events.jsonl unique.jsonl --key user.id --key type` keeps the first record for each user/type pair.

## ⚡ Quick Start
```bash
python main.py events.jsonl unique.jsonl
python main.py events.jsonl unique-by-user.jsonl --key user.id
```

## 🧰 Tech Stack
Python 3.10+ and the standard-library `json`, `argparse`, and `pathlib` modules.

## 🗂️ Folder Structure
```text
.
├── main.py
├── requirements.txt
├── tests/test_main.py
├── assets/icon.svg
├── .gitignore
└── LICENSE
```

## 🧭 Roadmap
- [ ] Add a dry-run mode
- [ ] Add optional output statistics as JSON
- [ ] Add a configurable canonicalization policy

## 🤝 Contributing
Issues and focused pull requests are welcome. Include tests for key selection and malformed input handling.

## 📄 License
Released under the [MIT License](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:14b8a6&height=100&section=footer" width="100%" alt="Animated wave footer"/></div>
