---
description: |
  Impacket's rpcdump.py enumerates Remote Procedure Call (RPC) endpoints.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

command: |
  python3 rpcdump.py test.local/john:password123@10.10.10.1
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
  - https://github.com/SecureAuthCorp/impacket/blob/master/examples/rpcdump.py
  - https://www.hackingarticles.in/impacket-guide-smb-msrpc/
---
