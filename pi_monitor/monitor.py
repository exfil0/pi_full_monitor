import time
import psutil
from rich.console import Console
from rich.table import Table
from .utils import format_size, get_top_processes


def get_cpu_temperature():
    """Retrieve the CPU temperature."""
    temps = psutil.sensors_temperatures()
    if "cpu_thermal" in temps:
        return f"{temps['cpu_thermal'][0].current:.2f}°C"
    else:
        return "N/A"


def main():
    console = Console()

    try:
        while True:
            console.clear()

            # General system stats
            table = Table(title="Raspberry Pi Performance Monitor", expand=True)
            table.add_column("Metric", style="bold cyan")
            table.add_column("Value", style="bold green")

            # CPU
            table.add_row("CPU Usage", f"{psutil.cpu_percent()}%")
            table.add_row("CPU Temp", get_cpu_temperature())

            # Memory
            memory = psutil.virtual_memory()
            table.add_row("Memory Usage", f"{memory.percent}% ({format_size(memory.used)}/{format_size(memory.total)})")

            # Disk
            disk = psutil.disk_usage('/')
            table.add_row("Disk Usage", f"{disk.percent}% ({format_size(disk.used)}/{format_size(disk.total)})")

            # Network
            net = psutil.net_io_counters()
            table.add_row("Network Sent", format_size(net.bytes_sent))
            table.add_row("Network Received", format_size(net.bytes_recv))

            console.print(table)

            # Top processes
            top_processes_table = get_top_processes()
            console.print(top_processes_table)

            # Refresh every 2 seconds
            time.sleep(2)

    except KeyboardInterrupt:
        console.print("\n[bold red]Exiting Monitor... Goodbye![/]")
