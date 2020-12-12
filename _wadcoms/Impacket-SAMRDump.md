---
description: |
  Impacket's samrdump.py communicates with the Security Account Manager Remote (SAMR) interface to list system user accounts, available resource shares, and other sensitive information.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

command: |
  python3 samrdump.py test.local/john:password123@10.10.10.1
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
  - https://github.com/SecureAuthCorp/impacket/blob/master/examples/samrdump.py
  - https://www.hackingarticles.in/impacket-guide-smb-msrpc/
---
