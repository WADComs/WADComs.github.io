---
description: |
  Impacket's samrdump.py communicates with the Security Account Manager Remote (SAMR) interface to list system user accounts, available resource shares, and other sensitive information. 

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

functions:
  Password:
    - code: |
        python3 samrdump.py test.local/john:password123@10.10.10.1
  Username:
    - code: |
        empty
  RPC:
    - code: |
        empty
---
