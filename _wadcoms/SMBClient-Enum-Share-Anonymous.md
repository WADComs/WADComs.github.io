---
description: |
  Smbclient is a tool used to communicate with SMB servers. The following command will connect to an SMB share `public` using anonymous login.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	SMB Share: public

items:
  No_Creds:
    - code: |
        smbclient \\\\test.local\\public -I 10.10.10.1 -N
filters:
  Enumeration:
    - code: |
        empty
  SMB:
    - code: |
  Linux:
    - code: |
        empty
---
