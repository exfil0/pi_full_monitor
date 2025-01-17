# Updated utils.py

import psutil
from rich.table import Table

def format_bytes(bytes_value):
    """Convert bytes to a human-readable format."""
    if bytes_value is None:
        return "N/A"
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if bytes_value < 1024.0:
            return f"{bytes_value:.2f} {unit}"
        bytes_value /= 1024.0


def get_top_processes(limit=5):
    """Retrieve top processes by CPU and memory usage."""
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processes.sort(key=lambda x: x['cpu_percent'], reverse=True)
    return processes[:limit]


def check_device_status():
    """Check if specific devices are connected."""
    devices = {
        "RTL-SDR": "rtl_test",
        "HackRF": "hackrf_info",
        "Airspy": "airspy_info",
        "BladeRF": "bladeRF-cli -e version",
    }
    statuses = {}
    for device, command in devices.items():
        try:
            result = psutil.Popen(command, shell=True, stdout=psutil.PIPE, stderr=psutil.PIPE)
            result.communicate(timeout=2)
            statuses[device] = "Connected"
        except Exception:
            statuses[device] = "Disconnected"

    return statuses
