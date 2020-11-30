---
description: |
  ropnop's kerbrute bruteforces and enumerates valid Active Directory accounts through Kerberos Pre-Authentication. The following command will attempt to brute force valid username and passwords logins given a list of credentials (in the format `username:password`).

  Command Reference:

  	Domain: test.local

  	Credential List: credentials.txt
items:
  No_Creds:
    - code: |
        cat credentials.txt | kerbrute_linux_amd64 -d test.local bruteforce -
filters:
  Kerberos:
    - code: |
        empty
  Linux:
    - code: |
        empty
---
