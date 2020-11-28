---
description: |
  Impacket's reg.py is a remote registry manipulation tool, providing similar functionality to reg.exe in Windows.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

functions:
  Password:
    - code: |
        python3 reg.py test.local/john:password123@10.10.10.1 query -keyName HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows -s
  Username:
    - code: |
        empty
  SMB:
    - code: |
        empty
---
