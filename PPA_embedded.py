import psutil
import subprocess
import socket
import tkinter as tk
from tkinter import messagebox
from tkinter import *

def get_cpu_info():
    # CPU information
    cpu_info = f"CPU Cores: {psutil.cpu_count(logical=False)}\nCPU Threads: {psutil.cpu_count(logical=True)}"

    total_cpu_percent = psutil.cpu_percent(interval=1)
    cpu_usage_info = f"\nTotal CPU Usage: {total_cpu_percent}%"
    Processor_Num = Processor_Num_Info()

    return f"CPU Information:\n{cpu_info}{cpu_usage_info}{Processor_Num}\n"

def Processor_Num_Info():
    try:
        processes = psutil.process_iter()
        num_processes = sum(1 for _ in processes)

        return f"\nTotal Processes: {num_processes}"
    except Exception as e:
        return f"Error: {e}"

def get_memory_info():
    # Memory information
    mem_info = f"Total RAM installed: {convert_bytes(psutil.virtual_memory().total)}"

    # Detailed memory usage
    mem_usage = psutil.virtual_memory()
    mem_usage_info = f"\nRAM Usage:\n  Total: {convert_bytes(mem_usage.total)}\n  Used: {convert_bytes(mem_usage.used)}\n  Free: {convert_bytes(mem_usage.free)}\n  Percent: {mem_usage.percent}%"


    return f"Memory Information:\n{mem_info}{mem_usage_info}"

def get_disk_info():
    disk_info = ""
    for partition in psutil.disk_partitions():
        usage = psutil.disk_usage(partition.mountpoint)
        disk_info += f"\nPartition: \"{partition.device}\" Total Space: {convert_bytes(usage.total)}, Used: {convert_bytes(usage.used)}, Free: {convert_bytes(usage.free)}, Usage: {usage.percent}%"
    return f"\nDisk Information:{disk_info}\n"

def get_network_info():
    try:
        ipv4 = socket.gethostbyname(socket.gethostname())

        ipv6 = None
        for addr_info in socket.getaddrinfo(socket.gethostname(), None):
            if addr_info[1] == socket.AF_INET6:
                ipv6 = addr_info[4][0]
                break

        subnet_mask = None
        for interface, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                if addr.family == socket.AF_INET and addr.address == ipv4:
                    subnet_mask = addr.netmask
                    break

        return f"Network Information:\nipv4: {ipv4}\nipv6: {ipv6}\nSubnet mask: {subnet_mask}"
    except Exception as e:
        return f"Error: {e}"

def convert_bytes(byte_size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if byte_size < 1024.0:
            break
        byte_size /= 1024.0
    return f"{byte_size:.1f} {unit}"

if __name__ == "__main__":
    CPU_info = get_cpu_info()
    MEM_info = get_memory_info()
    DSK_info = get_disk_info()
    NET_info = get_network_info()
    print(f"{CPU_info}\n{MEM_info}\n{DSK_info}\n{NET_info}")