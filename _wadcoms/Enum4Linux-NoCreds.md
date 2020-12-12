---
description: |
  Enum4Linux is a tool for enumerating information from Windows and Samba systems, using a number of different techniques. The following command will attempt to enumerate information using no credentials.

  Command Reference:

  	Target IP: 10.10.10.1

command: |
  enum4linux -a 10.10.10.1
items:
  - No_Creds
attack_types:
  - Enumeration
OS:
  - Linux
references:
  - https://github.com/CiscoCXSecurity/enum4linux
---
