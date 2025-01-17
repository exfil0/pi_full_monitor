from rich.console import Console
from rich.table import Table
from rich.live import Live
import psutil
from utils import format_bytes, get_top_processes, check_device_status


def get_system_metrics():
    """Retrieve system metrics."""
    metrics = {
        "CPU Usage": f"{psutil.cpu_percent()}%",
        "CPU Temp": f"{psutil.sensors_temperatures().get('cpu_thermal', [{'current': 'N/A'}])[0]['current']}°C",
        "Memory Usage": f"{psutil.virtual_memory().percent}% ({format_bytes(psutil.virtual_memory().used)} / {format_bytes(psutil.virtual_memory().total)})",
        "Disk Usage": f"{psutil.disk_usage('/').percent}% ({format_bytes(psutil.disk_usage('/').used)} / {format_bytes(psutil.disk_usage('/').total)})",
        "Network Sent": format_bytes(psutil.net_io_counters().bytes_sent),
        "Network Received": format_bytes(psutil.net_io_counters().bytes_recv),
    }
    return metrics


def get_device_status():
    """Check for connected devices."""
    devices = [
        {"command": "hackrf_info", "name": "HackRF"},
        {"command": "rtl_test -t", "name": "RTL-SDR"},
        {"command": "airspy_info", "name": "Airspy"},
        {"command": "bladeRF-cli -e info", "name": "bladeRF"},
    ]
    return [check_device_status(device["command"], device["name"]) for device in devices]


def render_dashboard():
    """Render the dashboard with system metrics and connected devices."""
    console = Console()
    table = Table(title="Raspberry Pi Full Monitor", style="bold green")
    table.add_column("Metric", style="cyan", justify="right")
    table.add_column("Value", style="magenta", justify="left")

    metrics = get_system_metrics()
    for key, value in metrics.items():
        table.add_row(key, value)

    device_statuses = get_device_status()
    table.add_row("Devices", "\n".join(device_statuses))

    process_table = Table(title="Top Processes", style="bold blue")
    process_table.add_column("PID", justify="right")
    process_table.add_column("Name", justify="left")
    process_table.add_column("CPU %", justify="right")
    process_table.add_column("Memory %", justify="right")

    for proc in get_top_processes():
        process_table.add_row(str(proc['pid']), proc['name'], f"{proc['cpu_percent']}%", f"{proc['memory_percent']}%")

    return table, process_table


def main():
    """Main function to display the live dashboard."""
    with Live(auto_refresh=True, screen=True) as live:
        while True:
            dashboard, process_table = render_dashboard()
            live.update(dashboard)
            live.console.print(process_table)
            live.console.print("\nPress Ctrl+C to exit.")
            time.sleep(2)
