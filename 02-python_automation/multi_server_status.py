import socket

servers = [("8.8.8.8", 53) , ("127.0.0.1", 8000), ("198.168.99.90", 80)]

print("\n===================================================")
print("        REAL-TIME CLOUD INFRUSTRUCTURE AUDIT    ")
print("===================================================\n")





for ip, port in servers:
    print(f"Varifying network socket -> [ {ip}:{port} ]")


    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.settimeout(2)

    result = sock.connect_ex((ip, port))
    sock.close()

    if result == 0:
        print(f"Status: ONLINE | Server Is Helthy.\n")
    else:
        print(f"Status: DOWN!!! | Alert Send To DevOps!\n")


print("======================================================\n")
print("       MONITORING COMPLETED BY | SHAKIL       ")
print("\n======================================================")
