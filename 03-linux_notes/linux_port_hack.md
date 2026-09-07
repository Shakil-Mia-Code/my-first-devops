# Advanced Linux Network Port Diagnostics & Kernel Bypass
Today I mastered alternative verification techniques under strict kernel network sandbox rules.
1. 'nohup python3 -m http.server 8000 &' - Deployed a live python listener process on Port 8000.
2. Identified Android netlink socket isolation blockades (Permission Denied on ss/netstat tools).
3. 'curl http://127.0.0.1:8000' - Successfully bypassed core socket blockades to trigger local application response loops.
Successfully completed Linux Network Port Hacking Lab.
