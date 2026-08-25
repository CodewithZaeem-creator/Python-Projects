import platform
import shutil


def run():
    print("\n=== SYSTEM DIAGNOSTICS ===")
    print("OS:", platform.system(), platform.release())
    print("Machine:", platform.machine())
    print("Python:", platform.python_version())
    total, used, free = shutil.disk_usage('.')
    print(f"Disk free: {free / (1024**3):.1f} GB")
