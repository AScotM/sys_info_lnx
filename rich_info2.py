import platform
import os
import psutil
import time
import socket
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

    # Add disk usage information
    disk_usage = psutil.disk_usage('/')
    table.add_row("Disk Usage", f"{disk_usage.percent}% used ({disk_usage.used / (1024**3):.2f} GB used, {disk_usage.free / (1024**3):.2f} GB free)")

    # Add CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    table.add_row("CPU Usage", f"{cpu_usage}%")

    # Add system uptime
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_str = str(time.strftime("%H:%M:%S", time.gmtime(uptime_seconds)))
    table.add_row("Uptime", uptime_str)

    # Add Python version
    table.add_row("Python Version", platform.python_version())

    # Add swap memory usage
    swap_memory = psutil.swap_memory()
    table.add_row("Swap Memory", f"{swap_memory.percent}% used ({swap_memory.used / (1024**3):.2f} GB used, {swap_memory.free / (1024**3):.2f} GB free)")

    # Optionally, add battery status (if applicable)
    if psutil.sensors_battery():
        battery = psutil.sensors_battery()
        table.add_row("Battery", f"{battery.percent}% - {'Charging' if battery.power_plugged else 'Discharging'}")

    # Add network interfaces
    net_if_addrs = psutil.net_if_addrs()
    for iface, addrs in net_if_addrs.items():
        for addr in addrs:
            if addr.family == socket.AF_INET:  # Use socket.AF_INET instead of psutil.AF_INET
                table.add_row(f"Network Interface ({iface})", addr.address)

    console.print(table)

if __name__ == "__main__":
    display_system_info()

