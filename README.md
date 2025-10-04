# Lab 01: Python Scripting for IT Automation

## Overview

This lab demonstrates practical Python scripting skills for automating common IT operational tasks. Participants will develop scripts to handle file system operations, log analysis, and basic system health checks, showcasing their ability to write efficient and reusable automation solutions.

## Technologies Used

*   Python 3.x
*   Standard Python Libraries (e.g., `os`, `shutil`, `logging`, `re`)
*   Git & GitHub (for version control and collaboration)

## Learning Objectives

Upon completion of this lab, you will be able to:

*   Write Python scripts to automate file and directory management.
*   Develop scripts for parsing and analyzing log files.
*   Implement basic system health checks using Python.
*   Utilize command-line arguments for script flexibility.
*   Organize Python code into modular functions.

## Lab Structure

The repository is structured as follows:

```
.gitignore
README.md
requirements.txt
scripts/
├── file_organizer.py
├── log_analyzer.py
└── system_health_check.py
```

## Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/01-python-automation.git
    cd 01-python-automation
    ```
2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Lab Tasks

### Task 1: File Organizer Script

Develop `scripts/file_organizer.py` that:

*   Takes a directory path as a command-line argument.
*   Organizes files within that directory into subdirectories based on their file extension (e.g., `.txt` files go into a `Text` folder, `.jpg` into `Images`).
*   Handles existing directories and creates new ones as needed.
*   Includes error handling for invalid paths.

### Task 2: Log Analyzer Script

Develop `scripts/log_analyzer.py` that:

*   Takes a log file path as a command-line argument.
*   Parses the log file to extract specific information (e.g., error messages, warning counts, IP addresses).
*   Generates a summary report (e.g., to console or a new file) of the findings.
*   Demonstrates the use of regular expressions for pattern matching.

### Task 3: System Health Check Script

Develop `scripts/system_health_check.py` that:

*   Checks basic system metrics (e.g., CPU usage, memory usage, disk space).
*   Reports the status of specified services (e.g., `apache2`, `nginx` on Linux).
*   Outputs a clear, human-readable status report.
*   Can be configured to run periodically (e.g., via cron job - *optional, for advanced users*).

## Expected Outcome

Successful completion of this lab will result in three functional Python scripts that demonstrate practical automation skills. The `README.md` should be updated with examples of how to run each script and their expected output.

## Contribution

Feel free to fork this repository, implement your solutions, and submit pull requests. Constructive feedback and improvements are always welcome.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

