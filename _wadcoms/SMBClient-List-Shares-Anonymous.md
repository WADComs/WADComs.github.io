---
description: |
  Smbclient is a tool used to communicate with SMB servers. The following command will list out all available shares on the target server using anonymous login.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

items:
  No_Creds:
    - code: |
        smbclient -L \\test.local -I 10.10.10.1 -N
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
