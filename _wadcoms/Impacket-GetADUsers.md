---
description: |
  Impacket's GetADUsers.py will attempt to gather data about the domain's users and their corresponding email addresses.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

command: |
  python3 GetADUsers.py -all test.local/john:password123 -dc-ip 10.10.10.1
items:
  - Username
  - Password
services:
  - Kerberos
attack_types:
  - Enumeration
OS:
  - Linux
  - Windows
references:
  - https://github.com/SecureAuthCorp/impacket/blob/master/examples/GetADUsers.py
---
