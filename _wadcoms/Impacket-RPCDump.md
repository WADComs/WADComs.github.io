---
description: |
  Impacket's rpcdump.py enumerates Remote Procedure Call (RPC) endpoints.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

items:
  Password:
    - code: |
        python3 rpcdump.py test.local/john:password123@10.10.10.1
  Username:
    - code: |
        empty
filters:
  RPC:
    - code: |
        empty
---
