---
description: |
  ropnop's kerbrute bruteforces and enumerates valid Active Directory accounts through Kerberos Pre-Authentication. The following command will attempt to enumerate valid usernames given a list of usernames to try.

  Command Reference:

  	Domain: test.local

  	Username List: usernames.txt
items:
  No_Creds:
    - code: |
        kerbrute userenum -d test.local usernames.txt
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
