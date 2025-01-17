import psutil
from rich.console import Console
from rich.table import Table
from .utils import format_size, get_top_processes

def main():
    console = Console()

    while True:
        console.clear()

        # General system stats
        table = Table(title="Raspberry Pi Performance Monitor", expand=True)
        table.add_column("Metric", style="bold cyan")
        table.add_column("Value", style="bold green")

        # CPU
        table.add_row("CPU Usage", f"{psutil.cpu_percent()}%")
        table.add_row("CPU Temp", f"{psutil.sensors_temperatures().get('cpu_thermal', [{'current': 'N/A'}])[0]['current']}°C")
        
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

        console.input("\nPress [bold cyan]Enter[/] to refresh...")
