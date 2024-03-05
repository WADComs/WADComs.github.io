---
description: |
  "NetExec (a.k.a nxc) is a network service exploitation tool that helps automate assessing the security of large networks." - https://www.netexec.wiki/. This command will execute a powershell command on the target machine if the user has Administrator privileges. using "-x" will execute from cmd.

  Command Reference:

  	Target IP: 10.10.10.1

  	Username: john

  	Password: password123

command: |
  nxc smb 10.10.10.1 -u 'john' -p 'password123' -X '$Host'
items:
  - Username
  - Password
services:
  - SMB
attack_types:
  - Exploitation
OS:
  - Linux
references:
  - https://github.com/Pennyw0rth/NetExec
  - https://www.netexec.wiki/
---
