import socket
import os
from datetime import datetime

cloud_servers = [

    {"name":  "Google_Core_DNS" , "ip": "8.8.8.8", "port": 53},
    {"name": "Riyad_DB_Node", "ip": "192.168.88.88", "port": 3306},
    {"name": "Payment_Gatway", "ip": "10.0.0.99", "port": 88}
]

report_filename = "insfrastructure_health_report.txt"
current_time = datetime.now().strftime("Y%-%m-%d %H:%M:%S")


print("=================================================")
print("      DEVOPS ENTERPRISE  CAPSTONE MONITIRING     ")
print("=================================================")


with open (report_filename, "w") as report_file:

    report_file.write("\n====================================")
    report_file.write(f" CLOUD AUDIT LOG- TIMESRMTAMP: {current_time}\n")
    report_file.write("====================================")


    for server in cloud_servers:
        print(f"Auditing network socket -> [ {server['name']} ]")

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)

            result = sock.connect_ex((server['ip'], server['port'] ))
            sock.close()

            if result == 0:
                status_msg = "HEALTH STATUS : ONLINE | System Operatinal."
            else:
                status_msg = "HEALTH STATUS : DOWN!! | Immediate Action Required!"
        except Exception as e:
            status_msg = f"HEALTH STATUS : CRASHED | Error : {str(e)}"

        print(f"{status_msg}\n")


        report_file.write(f"SERVER NODE : {server['name']} ({server['ip']}:{server['port']})")
        report_file.write(f"{status_msg}\n")
        report_file.write("-------------------------------\n")

    print("\n   AUDIT COMLETED SUCCESSFULLY BY | ENGINEER SHAKIL.\n")


print("\n===============================================")
print(" REPORT CHRONICLED TO HARD DISK FILE.")
print("=================================================\n")
