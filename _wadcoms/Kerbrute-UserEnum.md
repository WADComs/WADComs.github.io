---
description: |
  ropnop's kerbrute bruteforces and enumerates valid Active Directory accounts through Kerberos Pre-Authentication. The following command will attempt to enumerate valid usernames given a list of usernames to try.

  Command Reference:

  	Domain: test.local

  	Username List: usernames.txt
command: |
  kerbrute userenum -d test.local usernames.txt
items:
  - No_Creds
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
