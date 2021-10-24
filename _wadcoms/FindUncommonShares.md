---
description: |
  The script FindUncommonShares.py is a Python equivalent of PowerView's Invoke-ShareFinder.ps1 allowing to quickly find uncommon shares in vast Windows Domains.

  Command Reference:

  	Target IP: 10.10.10.1

  	Attacker IP: 10.10.10.2

  	Domain: test.local

  	Username: john

  	Password: password123

command: |
  python3 FindUncommonShares.py -u 'john' -d 'TEST.local' -p 'password123' --dc-ip 10.10.10.1
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
  - Enumeration
references:
  - https://github.com/p0dalirius/FindUncommonShares
---
