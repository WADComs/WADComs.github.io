---
description: |
  windapsearch enumerates users, groups, and computers from a Windows domain through LDAP queries. The following command enumerates all 3 of the above mentioned using provided credentials.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

  	Enum Users: -U

  	Enum Groups: -G

  	Enum Domain Admins: --da

  	Enum members of group: -m "Remote Desktop Users"

  	Enum Computers and resolve DNS: -C -r

command: |
  python3 windapsearch --dc-ip 10.10.10.1 -u test.local\\john -p password123 -U -G --da -m "Remote Desktop Users" -C -r
items:
  - Username
  - Password
attack_types:
  - Enumeration
OS:
  - Linux
  - Windows
references:
  - https://github.com/ropnop/windapsearch
  - https://www.attackdebris.com/?p=470
---
