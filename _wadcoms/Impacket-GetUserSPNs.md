---
description: |
  Impacket's GetUserSPNs.py will attempt to fetch Service Principal Names that are associated with normal user accounts. What is returned is a ticket that is encrypted with the user account's password, which can then be bruteforced offline.

  Command Reference:

  	Target IP: 10.10.10.1
  
  	Domain: test.local

  	Username: john

  	Password: password123

items:
  Password:
    - code: |
        python3 GetUserSPNs.py test.local/john:password123 -dc-ip 10.10.10.1 -request
  Username:
    - code: |
        empty
filters:
  Kerberos:
    - code: |
        empty
---
