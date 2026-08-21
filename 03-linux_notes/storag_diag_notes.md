# Advanced Linux File Searching & Storage Diagnostics
Today I mastered server storage troubleshooting and identified disk space consumption.
1. 'find /usr -type f -size +10M' - Forces Linux to find files larger than 10MB while filtering out permission errors.
2. 'du -sh /usr/*' - Disk Usage summary in human-readable format. Successfully detected that /usr/lib was consuming 1.3GB of space!
Successfully mastered Advanced Linux Storage Diagnostics.
