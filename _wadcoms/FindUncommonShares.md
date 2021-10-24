---
description: |
  

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
  - Exploitation
references:
  - https://github.com/p0dalirius/FindUncommonShares
  - https://www.praetorian.com/blog/active-directory-computer-account-smb-relaying-attack
---
