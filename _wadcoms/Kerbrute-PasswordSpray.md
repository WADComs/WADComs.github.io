---
description: |
  ropnop's kerbrute bruteforces and enumerates valid Active Directory accounts through Kerberos Pre-Authentication. The following command will perform a password spray account against a list of provided users given a password.

  Command Reference:

  	Domain: test.local

  	Username List: domain_users.txt

  	Password: password123
command: |
  kerbrute passwordspray -d test.local domain_users.txt password123
items:
  - Username
services:
  - Kerberos
OS:
  - Linux
  - Windows
attack_types:
  - Enumeration
references:
  - https://github.com/ropnop/kerbrute
---
