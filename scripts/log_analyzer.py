#!/usr/bin/env python3

import re
import sys
from collections import Counter

def analyze_log(log_file_path):
    """
    Analyzes a log file to extract error messages, warning counts, and IP addresses.
    """
    if not sys.stdin.isatty(): # Check if input is being piped
        log_content = sys.stdin.read()
    elif not log_file_path or not os.path.exists(log_file_path):
        print(f"Error: Log file not found at {log_file_path}")
        sys.exit(1)
    else:
        with open(log_file_path, 'r') as f:
            log_content = f.read()

    error_pattern = re.compile(r"ERROR: (.*)")
    warning_pattern = re.compile(r"WARNING: (.*)")
    ip_pattern = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")

    errors = error_pattern.findall(log_content)
    warnings = warning_pattern.findall(log_content)
    ips = ip_pattern.findall(log_content)

    print("\n--- Log Analysis Report ---")
    print(f"Total Errors: {len(errors)}")
    for error in errors:
        print(f"  - {error}")

    print(f"\nTotal Warnings: {len(warnings)}")
    for warning in warnings:
        print(f"  - {warning}")

    print("\nTop 5 IP Addresses:")
    if ips:
        ip_counts = Counter(ips)
        for ip, count in ip_counts.most_common(5):
            print(f"  - {ip}: {count} occurrences")
    else:
        print("  No IP addresses found.")

    print("\n--- Report End ---")

if __name__ == "__main__":
    import os
    if len(sys.argv) > 1:
        log_file = sys.argv[1]
        analyze_log(log_file)
    elif not sys.stdin.isatty(): # Check if input is being piped
        analyze_log(None) # Pass None or handle piped input directly
    else:
        print("Usage: python log_analyzer.py <log_file_path>")
        print("       Or pipe content: cat logfile.log | python log_analyzer.py")
        sys.exit(1)

