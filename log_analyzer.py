log_file_path = "app_server.log"

print("\n===============================================")
print("      -ENTERPRISE LIVE LOG ANALYZER ENGEEN-      ")
print("=================================================")


with open (log_file_path, "r") as file:

    for line in file:

        if "ERROR" in line or "CRITICAL" in line:
            print(f"ALERT DETECTED -> {line.strip()}")




print("================================================")
print("   -ANALYSIS COMPLETED BY | ENGINEER SHAKIL-    ")
print("==============================================\n")
