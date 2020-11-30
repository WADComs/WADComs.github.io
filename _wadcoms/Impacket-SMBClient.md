---
description: |
  Impacket's smbclient.py is a generic smbclient, allowing you to list shares and files, rename, upload and download files and create and delete directories.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

items:
  Password:
    - code: |
        python3 smbclient.py test.local/john:password123@10.10.10.1
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
