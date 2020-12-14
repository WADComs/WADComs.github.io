---
description: |
  Impacket's addcomputer.py will add a computer account to the domain and set its password. The following command will create a new computer over LDAPS. Plain LDAP is not supported, as it doesn't allow setting the password of the new computer.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	New Computer Password: TestPassword123

  	New Computer Name: testComputer

  	Username: john

  	Password: password123

command: |
  python3 addcomputer.py -method LDAPS -dc-ip 10.10.10.1 -computer-pass TestPassword321 -computer-name testComputer test.local/john:password123
items:
  - Username
  - Password
services:
  - LDAP
OS:
  - Linux
  - Windows
attack_types:
  - Exploitation
  - Persistence
references:
  - https://github.com/SecureAuthCorp/impacket/blob/master/examples/addcomputer.py
  - http://blog.redxorblue.com/2019/12/no-shells-required-using-impacket-to.html
---
