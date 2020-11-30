---
description: |
  Impacket's services.py communicates with Windows services using the MSRPC interface. It can perform many different actions on any service.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

  	Action: list

items:
  Password:
    - code: |
        python3 services.py test.local/john:password123@10.10.10.1 list
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
