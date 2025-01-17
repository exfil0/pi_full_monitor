import psutil
from rich.table import Table

def format_size(size):
    """Convert bytes to a human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

def get_top_processes(limit=10):
    """Get a table of top processes by CPU usage."""
    processes = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']),
                       key=lambda p: p.info['cpu_percent'],
                       reverse=True)[:limit]

    table = Table(title="Top Processes", expand=True)
    table.add_column("PID", style="bold cyan")
    table.add_column("Name", style="bold green")
    table.add_column("CPU %", style="bold yellow")
    table.add_column("Memory %", style="bold magenta")

    for proc in processes:
        try:
            table.add_row(str(proc.info['pid']),
                          proc.info['name'],
                          f"{proc.info['cpu_percent']:.2f}%",
                          f"{proc.info['memory_percent']:.2f}%")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return table
