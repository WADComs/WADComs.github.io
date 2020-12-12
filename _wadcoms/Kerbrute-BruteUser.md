---
description: |
  ropnop's kerbrute bruteforces and enumerates valid Active Directory accounts through Kerberos Pre-Authentication. The following command will bruteforce an account against a list of provided passwords given a username.

  Command Reference:

  	Domain: test.local

  	Password List: passwords.txt

  	Username: john
command: |
  kerbrute bruteuser -d test.local passwords.txt john
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
