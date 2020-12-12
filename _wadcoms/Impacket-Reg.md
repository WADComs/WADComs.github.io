---
description: |
  Impacket's reg.py is a remote registry manipulation tool, providing similar functionality to reg.exe in Windows.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

command: |
  python3 reg.py test.local/john:password123@10.10.10.1 query -keyName HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows -s
items:
  - Password
  - Username
services:
  - SMB
OS:
  - Linux
  - Windows
attack_types:
  - Exploitation
  - Persistence
references:
  - https://github.com/SecureAuthCorp/impacket/blob/master/examples/reg.py
  - https://www.hackingarticles.in/impacket-guide-smb-msrpc/
---
