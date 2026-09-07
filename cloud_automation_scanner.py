import socket

cloud_infrastructure = [
    {"name": "Google-Primary-DNS" , "ip": "8.8.8.8", "port": 53},
    {"name": "Localhost-Gateway", "ip": "127.0.0.1", "port": 8000},
    {"name": "Riyad-Backup-Node", "ip": "192.168.99.99", "port": 80}
]

print("\n==================================================")
print("       ENTERPRISE CLOUD INFRASTRUCTURE AUDIT    ")
print("===================================================")



for server in cloud_infrastructure:
    print(f"Scanning Node : [ {server['name']} ] ->  [ { server['ip']} ]:[ {server['port']} ]") 


    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)


    result = sock.connect_ex((server['ip'], server['port']))
    sock.close()

    if result == 0:
        print("Health Status: ONLINE | Connection secure\n")
    else:
        print("Health Status: DOWN!! | Alert Sent To DevOps!")

print("======================================================")
print("        SCAN COMPLETED BY |  ENGINEER SHAKIL           ")
print("======================================================\n")
