---
description: |
  ropnop's kerbrute bruteforces and enumerates valid Active Directory accounts through Kerberos Pre-Authentication. The following command will bruteforce an account against a list of provided passwords given a username.

  Command Reference:

  	Domain: test.local

  	Password List: passwords.txt

  	Username: john
items:
  Username:
    - code: |
        kerbrute bruteuser -d test.local passwords.txt john
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
