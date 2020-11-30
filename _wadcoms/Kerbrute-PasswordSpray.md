---
description: |
  ropnop's kerbrute bruteforces and enumerates valid Active Directory accounts through Kerberos Pre-Authentication. The following command will perform a password spray account against a list of provided users given a password.

  Command Reference:

  	Domain: test.local

  	Username List: domain_users.txt

  	Password: password123
items:
  Password:
    - code: |
        kerbrute passwordspray -d test.local domain_users.txt password123
filters:
  Kerberos:
    - code: |
        empty
  Linux:
    - code: |
        empty
  Windows:
    - code: |
        empty
---
