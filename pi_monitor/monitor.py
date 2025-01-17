import psutil
import platform
import shutil
import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.live import Live
from datetime import datetime

console = Console()

def get_system_info():
    uname = platform.uname()
    return {
        "System": uname.system,
        "Node Name": uname.node,
        "Release": uname.release,
        "Version": uname.version,
        "Machine": uname.machine,
        "Processor": uname.processor,
    }

def get_cpu_info():
    cpu_freq = psutil.cpu_freq()
    return {
        "Usage (%)": psutil.cpu_percent(interval=0.5),
        "Cores": psutil.cpu_count(logical=False),
        "Threads": psutil.cpu_count(logical=True),
        "Frequency (MHz)": round(cpu_freq.current, 2) if cpu_freq else "N/A",
    }

def get_memory_info():
    mem = psutil.virtual_memory()
    return {
        "Total (GB)": round(mem.total / (1024**3), 2),
        "Used (GB)": round(mem.used / (1024**3), 2),
        "Available (GB)": round(mem.available / (1024**3), 2),
        "Usage (%)": mem.percent,
    }

def get_disk_info():
    total, used, free = shutil.disk_usage("/")
    return {
        "Total (GB)": round(total / (1024**3), 2),
        "Used (GB)": round(used / (1024**3), 2),
        "Free (GB)": round(free / (1024**3), 2),
    }

def get_temperature():
    try:
        temps = psutil.sensors_temperatures()
        if "cpu_thermal" in temps:
            return f"{temps['cpu_thermal'][0].current}°C"
        return "N/A"
    except AttributeError:
        return "N/A"

def get_usb_devices():
    try:
        usb_devices = [f"{dev.device} - {dev.name}" for dev in psutil.disk_partitions()]
        return usb_devices if usb_devices else ["No USB devices connected"]
    except Exception:
        return ["Unable to fetch USB devices"]

def get_top_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    # Sort processes by CPU usage
    processes.sort(key=lambda x: x['cpu_percent'], reverse=True)
    return processes[:5]

def build_dashboard():
    table = Table(title=f"Raspberry Pi Dashboard - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    table.add_column("Category", justify="left", style="bold")
    table.add_column("Details", justify="left")

    # System Information
    sys_info = get_system_info()
    table.add_row("System Info", "\n".join([f"{k}: {v}" for k, v in sys_info.items()]))

    # CPU Information
    cpu_info = get_cpu_info()
    table.add_row("CPU Info", "\n".join([f"{k}: {v}" for k, v in cpu_info.items()]))

    # Memory Information
    mem_info = get_memory_info()
    table.add_row("Memory Info", "\n".join([f"{k}: {v}" for k, v in mem_info.items()]))

    # Disk Information
    disk_info = get_disk_info()
    table.add_row("Disk Info", "\n".join([f"{k}: {v}" for k, v in disk_info.items()]))

    # Temperature
    table.add_row("Temperature", get_temperature())

    # USB Devices
    usb_devices = get_usb_devices()
    table.add_row("USB Devices", "\n".join(usb_devices))

    # Top Processes
    top_processes = get_top_processes()
    process_table = Table(title="Top Processes", expand=True)
    process_table.add_column("PID", justify="right")
    process_table.add_column("Name", justify="left")
    process_table.add_column("CPU (%)", justify="right")
    process_table.add_column("Memory (%)", justify="right")

    for proc in top_processes:
        process_table.add_row(
            str(proc['pid']), proc['name'], f"{proc['cpu_percent']}%", f"{proc['memory_percent']}%"
        )

    return Panel(
        table, title="Raspberry Pi Performance Monitor", expand=True
    ), Panel(process_table, title="Resource-Intensive Processes", expand=True)

if __name__ == "__main__":
    with Live(auto_refresh=False, console=console, screen=True) as live:
        while True:
            dashboard, process_panel = build_dashboard()
            live.update(Panel.fit(dashboard, process_panel), refresh=True)
            time.sleep(1)
