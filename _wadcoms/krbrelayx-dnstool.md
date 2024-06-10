---
description: |
  Add/modify/delete Active Directory Integrated DNS records via LDAP.
  Requires impacket, ldap3 and dnspython to function. It is recommended to install impacket from git directly to have the latest version available.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

command: |
  python3 dnstool.py -u test.local\\john -p password123 --action add --record web01 --data 10.10.10.1 --type A test.local
items:
  - Username
  - Password
services:
  - Kerberos
  - LDAP
  - DNS
attack_types:
  - Exploitation
OS:
  - Linux
references:
  - https://github.com/dirkjanm/krbrelayx
---
