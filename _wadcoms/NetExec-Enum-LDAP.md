---
description: |
  "NetExec (a.k.a nxc) is a network service exploitation tool that helps automate assessing the security of large networks." - https://www.netexec.wiki/. This command will enumerate domain groups, local groups, users, user descriptions, users trusted for delegation, users without a password, You can also use CIDR notation to target a range of ip addresses (i.e. 10.10.10.0/24).

  Command Reference:

  	Target IP: 10.10.10.1

  	Username: john

  	Password: password123

command: |
  nxc ldap 10.10.10.1 -u 'john' -p 'password123' --trusted-for-delegation  --password-not-required --admin-count --users --groups
items:
  - Username
  - Password
services:
  - LDAP
attack_types:
  - Enumeration
OS:
  - Linux
references:
  - https://github.com/Pennyw0rth/NetExec
  - https://www.netexec.wiki/
---
