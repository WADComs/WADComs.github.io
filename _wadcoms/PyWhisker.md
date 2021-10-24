---
description: |
  pyWhisker is a tool allowing users to manipulate the msDS-KeyCredentialLink attribute of a target user/computer to obtain full control over that object. It's based on Impacket and on our Python equivalent of Michael Grafnetter's DSInternals called PyDSInternals. This tool, along with Dirk-jan's PKINITtools allow for a complete primitive exploitation on UNIX-based systems only.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

command: |
  python3 pywhisker.py -d "test.local" -u "john" -p "password123" --target "user2" --action "list" --dc-ip "10.10.10.1"
items:
  - Password
  - Username
services:
  - Kerberos
OS:
  - Linux
attack_types:
  - Exploitation
references:
  - https://github.com/shutdownrepo/pywhisker
---
