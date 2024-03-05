---
description: |
  "NetExec (a.k.a nxc) is a network service exploitation tool that helps automate assessing the security of large networks." - https://www.netexec.wiki/. This command will enumerate the SMB host using a null session. 

  Command Reference:

  	Target IP: 10.10.10.1

command: |
  nxc smb 10.10.10.1 -u '' -p ''
items:
  - No_Creds
services:
  - SMB
attack_types:
  - Enumeration
OS:
  - Linux
references:
  - https://github.com/Pennyw0rth/NetExec
  - https://www.netexec.wiki/
---
