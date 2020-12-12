---
description: |
  ropnop's kerbrute bruteforces and enumerates valid Active Directory accounts through Kerberos Pre-Authentication. The following command will attempt to brute force valid username and passwords logins given a list of credentials (in the format `username:password`).

  Command Reference:

  	Domain: test.local

  	Credential List: credentials.txt
command: |
  cat credentials.txt | kerbrute_linux_amd64 -d test.local bruteforce -
items:
  - No_Creds
services:
  - Kerberos
OS:
  - Linux
attack_types:
  - Enumeration
references:
  - https://github.com/ropnop/kerbrute
---
