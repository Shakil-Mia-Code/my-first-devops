import socket


def varify_live_node(server_name, ip, port):


    print("\n---------------------------------------------------")
    print(f"Auditing Remote Node : [ {server_name} ]")
    print(f"Terget Endpoint     :  {ip}:{port}")


    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)


    result = sock.connect_ex((ip, port))
    sock.close()


    if result == 0:
        print("HEALTH STATUS : [ ONLINE ] -> Conection Secure.")
    else:
        print("HEALTH STATUS : [ DOWN ]   -> Alert Sent To DevOps!")


    print("\n---------------------------------------------------")

    print("            Monitoring By | SHAKIL        \n ")

varify_live_node("Google_DNS_Primary", "8.8.8.8" , 53)
varify_live_node("Jeddah_Backup_Server", "198.158.12.15", 8080)
