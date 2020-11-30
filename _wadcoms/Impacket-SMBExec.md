---
description: |
  Impacket's smbexec.py. This will give you an interactive shell on the Windows host.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123
items:
  Password:
    - code: |
        python3 smbexec.py test.local/john:password123@10.10.10.1
  Username:
    - code: |
        empty
filters:
  SMB:
    - code: |
        empty
  Linux:
    - code: |
        empty
  Windows:
    - code: |
        empty
---
