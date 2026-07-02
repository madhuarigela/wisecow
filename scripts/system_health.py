import psutil

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

print(f"CPU Usage: {cpu}%")
print(f"Memory Usage: {memory}%")
print(f"Disk Usage: {disk}%")

if cpu > 80:
    print("ALERT: High CPU Usage")

if memory > 80:
    print("ALERT: High Memory Usage")

if disk > 80:
    print("ALERT: High Disk Usage")

print(f"Running Processes: {len(psutil.pids())}")