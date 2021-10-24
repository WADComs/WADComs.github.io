---
description: |
  ldapmonitor.py allows you to monitor creation, deletion and changes to LDAP objects live during your pentest.

  Command Reference:

  	Target IP: 10.10.10.1

  	Attacker IP: 10.10.10.2

  	Domain: test.local

  	Username: john

  	Password: password123

command: |
  python3 ldapmonitor.py -u 'john' -d 'TEST.local' -p 'password123' --dc-ip 10.10.10.1

items:
  - Password
  - Username
  - Hash
services:
  - LDAP
  - Kerberos
  - NTLM
OS:
  - Linux
attack_types:
  - Enumeration
references:
  - https://github.com/p0dalirius/LDAPmonitor/tree/master/python
---
