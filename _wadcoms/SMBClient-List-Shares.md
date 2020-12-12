---
description: |
  Smbclient is a tool used to communicate with SMB servers. The following command will list out all available shares on the target server using valid credentials.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

command: |
  smbclient -L \\test.local -I 10.10.10.1 -U john password123
items:
  - Username
  - Password
services:
  - SMB
OS:
  - Linux
attack_types:
  - Enumeration
references:
  - https://www.samba.org/samba/docs/current/man-html/smbclient.1.html
---
