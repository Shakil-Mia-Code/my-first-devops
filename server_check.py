import psutil
vm = psutil.virtual_memory()

total_gb = vm.total / (1024**3)
available_gb = vm.available / (1024**3)
used_gb = vm.used / (1024**3)

print("\n===============================================")
print(" \n  REAL-TIME CLOUD SERVER MONITOR ")
print("\n================================================")
print(f"Total System RAM     : {total_gb:.2f} GB")
print(f"Total System Used RAM: {used_gb:.2f} GB")
print(f" Available RAM       : {available_gb:.2f} GB")
print(f"Memory Using Rate    : {vm.percent}%")
print(f"================================================")

if vm.percent > 70:
    print("[ CRITICAL ALERT ] Server RAM Usage Is High!Take Action Immediately!")
else:
    print("[ HELTHY ] Server RAM Usage Is Normal.")
