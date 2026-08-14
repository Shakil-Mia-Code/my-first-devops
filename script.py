def check_server_health(engineer, ip, cpu):
    print(f"\n--- [LIVE CLOUD REPORT {ip} ---")
    print(f" Monitored By: {engineer}")
    if cpu > 80:
        print(f" STATUS; [ ALERT ] -> CPU load is {cpu}%. Server is overloading!")
    else:
        print(f" STATUS: [ HEALTHY ] -> CPU load is  {cpu}%. All systems is normal.")
print ("=== Welcome to DevOps Cloud Monitor ===")
name = input("Enter Your Name: ")
target_ip = input("Entet Server Ip Address: ")
cpu_input = int(input("Enter Current Cpu Usage (0-100): "))
check_server_health(name, target_ip, cpu_input)
