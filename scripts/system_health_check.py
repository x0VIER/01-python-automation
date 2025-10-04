#!/usr/bin/env python3

import psutil
import platform
import sys
import os

def get_system_health():
    """
    Gathers basic system health metrics.
    """
    health_report = {
        "OS": platform.system(),
        "OS_Version": platform.version(),
        "CPU_Usage_Percent": psutil.cpu_percent(interval=1),
        "Memory_Usage_Percent": psutil.virtual_memory().percent,
        "Disk_Usage_Percent": psutil.disk_usage("/").percent,
        "Running_Processes": len(psutil.pids())
    }
    return health_report

def check_service_status(service_name):
    """
    Checks the status of a given service (Linux-specific).
    """
    if platform.system() == "Linux":
        try:
            # Using systemctl for systemd-based systems
            status_output = os.popen(f"systemctl is-active {service_name}").read().strip()
            return status_output == "active"
        except Exception:
            return False
    return "N/A" # Not applicable for non-Linux systems or if service check fails

def main():
    print("--- System Health Check Report ---")
    health_data = get_system_health()
    for key, value in health_data.items():
        print(f"{key}: {value}")

    print("\n--- Service Status ---")
    # Example services to check (customize as needed)
    services_to_check = ["apache2", "nginx", "sshd"]
    for service in services_to_check:
        status = check_service_status(service)
        if status is True:
            print(f"Service [32m{service}[0m: Running")
        elif status is False:
            print(f"Service [31m{service}[0m: Stopped")
        else:
            print(f"Service {service}: {status}")

    print("\n--- Report End ---")

if __name__ == "__main__":
    # Ensure psutil is installed
    try:
        import psutil
    except ImportError:
        print("Error: psutil library not found. Please install it using: pip install psutil")
        sys.exit(1)
    main()

