# Super-Advanced Linux Kernel Runlevels & Boot Targets
Today I successfully audited system initialization baselines and systemd boot targets.
1. 'systemctl get-default' - Successfully extracted the primary boot profile (graphical.target).
2. 'ls -l /lib/systemd/system/*.target' - Deeply audited kernel initialization target descriptors.
