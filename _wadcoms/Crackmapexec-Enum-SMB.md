---
description: |
  "CrackMapExec (a.k.a CME) is a post-exploitation tool that helps automate assessing the security of large Active Directory networks." - https://github.com/byt3bl33d3r/CrackMapExec/wiki. This command will enumerate domain groups, local groups, logged on users, relative identifiers (RIDs), sessions, domain users, SMB shares/permissions, and get the domain password policy. You can also use CIDR notation to target a range of ip addresses (i.e. 10.10.10.0/24).

  Command Reference:

  	Target IP: 10.10.10.1

  	Username: john

  	Password: password123

command: |
  crackmapexec smb 10.10.10.1 -u 'john' -p 'password123' --groups --local-groups --loggedon-users --rid-brute --sessions --users --shares --pass-pol
items:
  - Username
  - Password
services:
  - SMB
attack_types:
  - Enumeration
OS:
  - Linux
references:
  - https://github.com/byt3bl33d3r/CrackMapExec
  - https://github.com/byt3bl33d3r/CrackMapExec/wiki
---
