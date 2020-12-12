---
description: |
  Evil-WinRM uses the Windows Management Instrumentation (WMI) to give you an interactive shell on the Windows host.

  Command Reference:

  	Target IP: 10.10.10.1

  	Username: john

  	Password: password123

command: |
  evil-winrm -i 10.10.10.1 -u john -p password123
items:
  - Password
  - Username
services:
  - WMI
OS:
  - Linux
  - Windows
attack_types:
  - Exploitation
references:
  - https://github.com/Hackplayers/evil-winrm
---
