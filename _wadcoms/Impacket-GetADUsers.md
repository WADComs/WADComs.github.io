---
description: |
  Impacket's GetADUsers.py will attempt to gather data about the domain's users and their corresponding email addresses.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

items:
  Username:
    - code: |
        python3 GetADUsers.py -all test.local/john:password123 -dc-ip 10.10.10.1
  Password:
    - code: |
        empty
filters:
  Kerberos:
    - code: |
        empty
  Enumeration:
    - code: |
        empty
  Linux:
    - code: |
        empty
  Windows:
    - code: |
        empty
---
