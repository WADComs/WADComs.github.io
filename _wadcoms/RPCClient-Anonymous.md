---
description: |
  rpcclient is a tool used for executing client side MS-RPC functions to manage Windows NT clients from Unix workstatios. From an offensive security standpoint, it can be used to enumerate users, groups, and other potentially sensitive information. The following command attempt to connect to the NetBIOS server anonymously, in order to enumerate using MS-RPC available commands/functions.

  Command Reference:

  	Target IP: 10.10.10.1

items:
  No_Creds:
    - code: |
        rpcclient -U '' -N 10.10.10.1
filters:
  Enumeration:
    - code: |
        empty
  RPC:
    - code: |
        empty
  Linux:
    - code: |
        empty
---
