---
description: |
  Impacket's services.py communicates with Windows services using the MSRPC interface. It can perform many different actions on any service.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

  	Action: list

command: |
  python3 services.py test.local/john:password123@10.10.10.1 list
items:
  - Password
  - Username
services:
  - RPC
OS:
  - Linux
  - Windows
attack_types:
  - Enumeration
references:
  - https://github.com/SecureAuthCorp/impacket/blob/master/examples/services.py
  - https://www.hackingarticles.in/impacket-guide-smb-msrpc/
---
