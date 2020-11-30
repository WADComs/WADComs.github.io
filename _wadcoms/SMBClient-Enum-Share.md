---
description: |
  Smbclient is a tool used to communicate with SMB servers. The following command will connect to an SMB share `C$` using valid credentials.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	SMB Share: C$

  	Username: john

  	Password: password123

items:
  Username:
    - code: |
        smbclient \\\\test.local\\C$ -I 10.10.10.1 -U john password123
  Password:
    - code: |
        empty
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
