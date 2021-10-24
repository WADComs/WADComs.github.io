---
description: |
  Python script to automatically extract and decrypt Group Policy Preferences (GPP) passwords using streams for carving files instead of mounting shares

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

command: |
  python3 Get-GPPPassword.py 'TEST.local/john:password123@DC01.TEST.local' -dc-ip 10.10.10.1
items:
  - Password
  - Username
  - Hash
services:
  - SMB
OS:
  - Linux
  - Windows
attack_types:
  - Exploitation
  - Enumeration
references:
  - https://github.com/SecureAuthCorp/impacket/blob/master/examples/Get-GPPPassword.py
  - https://podalirius.net/en/articles/exploiting-windows-group-policy-preferences/
---
