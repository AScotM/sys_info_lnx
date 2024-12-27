import platform
import os
import psutil
from rich.console import Console
from rich.table import Table

def display_system_info():
    console = Console()
    table = Table(title="System Information")

    table.add_column("Property", style="bold cyan")
    table.add_column("Value", style="bold green")

    system_info = platform.uname()

    table.add_row("System", system_info.system)
    table.add_row("Node Name", system_info.node)
    table.add_row("Release", system_info.release)
    table.add_row("Version", system_info.version)
    table.add_row("Machine", system_info.machine)
    table.add_row("Processor", system_info.processor or "N/A")
    table.add_row("CPU Count", str(os.cpu_count()))
    table.add_row("Memory", f"{psutil.virtual_memory().total / (1024**3):.2f} GB")

    console.print(table)

if __name__ == "__main__":
    display_system_info()

