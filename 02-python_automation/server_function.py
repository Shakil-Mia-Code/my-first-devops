def check_status(server_name, status):
    print("\n------------------------------------------")
    print(f"System Node Audit : [ {server_name} ]")


    if status == "ONLINE":
        print("HEALTH STATUS : [ HELTHY ] -> Service Operational.")
    else:
        print("HELATH STATUS : [ CRITICAL ] -> Immediate Action Required!")

    print("------------------------------------------------------")
    print("        Monitoring By | SHAKIL       ")

check_status("Database_Server_01", "ONLINE")
check_status("Payment_Gatway_02", "OFFLINE")
check_status("Ghaibandh_Server_05", "ONLINE")
check_status("Dhaka_Server_08", "OFFLINE")
check_status("Riyad_Server_45", "ONLINE")
