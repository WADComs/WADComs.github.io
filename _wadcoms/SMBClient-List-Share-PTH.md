---
description: |
  Smbclient is a tool used to communicate with SMB servers. The following command will list out all available shares on the target ip using user John hash on test domain.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Hash: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

command: |
  smbclient -L \\10.10.10.1 -U test.local/john --pw-nt-hash XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
items:
  - Username
  - Hash
services:
  - SMB
OS:
  - Linux
attack_types:
  - Enumeration
references:
  - https://www.samba.org/samba/docs/current/man-html/smbclient.1.html
---
