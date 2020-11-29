---
description: |
  ropnop's kerbrute bruteforces and enumerates valid Active Directory accounts through Kerberos Pre-Authentication. The following command will attempt to enumerate valid usernames given a list of usernames to try.

  Command Reference:

  	Domain: test.local

  	Username List: usernames.txt
items:
  No_Creds:
    - code: |
        kerbrute_linux_amd64 userenum -d test.local usernames.txt
filters:
  Kerberos:
    - code: |
        empty
---
