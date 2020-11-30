---
description: |
  Impacket's lookupsid.py performs bruteforcing of Windows SID's to identify users/groups on the remote target.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

items:
  Password:
    - code: |
        python3 lookupsid.py test.local/john:password123@10.10.10.1
  Username:
    - code: |
        empty
filters:
  RPC:
    - code: |
        empty
  Linux:
    - code: |
        empty
  Windows:
    - code: |
        empty
---
