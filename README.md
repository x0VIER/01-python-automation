# 🐍 Python Scripting for IT Automation

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

> **Automate the boring stuff.** This lab is all about writing Python scripts that actually save you time in real IT operations. No fluff, just practical automation that works.

## 🎯 What's This About?

Ever spent hours organizing files, parsing logs, or checking system health manually? Yeah, me too. That's why I built this lab—to show you how Python can handle all that tedious work while you grab a coffee.

You'll build three scripts that IT pros actually use:
- **File Organizer** - Automatically sorts files by type (no more messy downloads folder!)
- **Log Analyzer** - Digs through logs to find errors, warnings, and suspicious IPs
- **System Health Checker** - Monitors CPU, memory, disk space, and service status

## 🛠️ Tech Stack

- **Python 3.x** (the good stuff)
- Standard libraries: `os`, `shutil`, `logging`, `re`, `psutil`
- Git & GitHub for version control

## 🚀 Quick Start

```bash
# Clone this bad boy
git clone https://github.com/x0VIER/01-python-automation.git
cd 01-python-automation

# Set up a virtual environment (trust me, you want this)
python3 -m venv venv
source venv/bin/activate  # Windows? Use: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 💡 What You'll Learn

By the end of this, you'll be able to:
- Write Python scripts that actually solve real problems
- Parse and analyze log files like a pro
- Automate file management (because life's too short for manual sorting)
- Check system health without opening Task Manager
- Use command-line arguments to make your scripts flexible
- Write clean, modular code that doesn't make you cringe later

## 📂 Project Structure

```
01-python-automation/
├── scripts/
│   ├── file_organizer.py      # Sorts files by extension
│   ├── log_analyzer.py         # Extracts insights from logs
│   └── system_health_check.py  # Monitors system metrics
├── requirements.txt
└── README.md
```

## 🎮 How to Use

### File Organizer
Got a messy directory? This script organizes it by file type automatically.

```bash
python scripts/file_organizer.py /path/to/messy/folder
```

It'll create folders like `Images/`, `Documents/`, `Videos/` and move everything where it belongs.

### Log Analyzer
Need to find errors in a huge log file? This script does the heavy lifting.

```bash
python scripts/log_analyzer.py /path/to/your/logfile.log
```

It'll spit out a summary with error counts, warnings, and the most active IP addresses.

### System Health Check
Want to know if your system is about to explode? Run this.

```bash
python scripts/system_health_check.py
```

You'll get CPU usage, memory stats, disk space, and service status—all in one clean report.

## 📝 Lab Tasks

### Task 1: Build the File Organizer
Create a script that:
- Takes a directory path as input
- Sorts files into folders by extension (`.txt` → `Text/`, `.jpg` → `Images/`)
- Handles edge cases (files with no extension, existing folders)
- Doesn't crash when you give it a bad path

### Task 2: Build the Log Analyzer
Create a script that:
- Reads a log file and finds patterns
- Counts errors and warnings
- Extracts IP addresses using regex
- Outputs a clean, readable summary

### Task 3: Build the System Health Checker
Create a script that:
- Checks CPU, memory, and disk usage
- Monitors service status (like `apache2`, `nginx`)
- Outputs everything in a human-friendly format
- (Bonus) Can be scheduled with cron for periodic checks

## 🏆 Success Criteria

You'll know you nailed it when:
- All three scripts run without errors
- The file organizer actually organizes files
- The log analyzer finds real patterns in logs
- The health checker gives accurate system info
- Your code is clean enough that you'd show it to a recruiter

## 🤝 Contributing

Found a bug? Have a cool idea? PRs are welcome! Just fork this repo, make your changes, and submit a pull request.

## 📄 License

MIT License - do whatever you want with this code. Just don't blame me if something breaks 😄

## 🔗 Connect

Built by someone who got tired of doing things manually. If you found this useful, star the repo!

---

**Keywords:** Python automation, IT scripting, log analysis, system monitoring, file organization, DevOps, Python projects, automation scripts, system administration
