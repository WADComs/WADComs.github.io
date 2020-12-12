---
description: |
  Impacket's wmiexec.py uses the Windows Management Instrumentation (WMI) to give you an interactive shell on the Windows host.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123
command: |
  python3 wmiexec.py test.local/john:password123@10.10.10.1
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
  - https://github.com/SecureAuthCorp/impacket/blob/master/examples/wmiexec.py
  - https://riccardoancarani.github.io/2020-05-10-hunting-for-impacket/#wmiexecpy
---
