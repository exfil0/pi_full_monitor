### utils.py ###
import psutil
import subprocess


def format_bytes(size):
    """Convert bytes to a human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024


def get_top_processes(limit=5):
    """Fetch top processes sorted by CPU and memory usage."""
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        processes.append(proc.info)
    
    processes.sort(key=lambda x: x['cpu_percent'], reverse=True)
    return processes[:limit]


def check_device_status(command, device_name):
    """Check if a device is connected using a CLI command."""
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True, timeout=5)
        if result.returncode == 0:
            return f"{device_name}: Connected"
        else:
            return f"{device_name}: Not Connected"
    except Exception as e:
        return f"{device_name}: Error ({str(e)})"
