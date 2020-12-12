---
description: |
  Enum4Linux is a tool for enumerating information from Windows and Samba systems, using a number of different techniques. The following command will attempt to enumerate information provided valid login credentials.

  Command Reference:

  	Target IP: 10.10.10.1

  	Username: john

  	Password: password123

command: |
  enum4linux -u john -p password123 -a 10.10.10.1
items:
  - Username
  - Password
attack_types:
  - Enumeration
OS:
  - Linux
references:
  - https://github.com/CiscoCXSecurity/enum4linux
---
