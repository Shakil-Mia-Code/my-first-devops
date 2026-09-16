print("\n==============================================")
print("     CRASH-PROOF SERVER AUTOMATION SYSTEM       ")
print("================================================")

try:
    print("Attempting to open critical log_file...")
    with open("ghost_server.log", "r") as file:
        date = file.read()

    print("    File Processed Successfully    ")


except FileNotFoundError:
    print(" [ SAFE HANDLE ]  ALERT! The target log file is  missing from the system!")
    print("System Actiin : Creating an automatic ticket for the cloud infrastructure team.")


print("=================================================")
print("STATUS: System core remained alive and operational!")
print("=================================================\n")
