---
description: |
  "CrackMapExec (a.k.a CME) is a post-exploitation tool that helps automate assessing the security of large Active Directory networks." - https://github.com/byt3bl33d3r/CrackMapExec/wiki

  The following command will enumerate smb shares and their permissions. 

  Command Reference:

  	Target IP: 10.10.10.1
    
    Username: john
    
    Password: password123

command: |
  crackmapexec smb 10.10.10.1 -u 'john' -p 'password123' --shares
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
  - https://github.com/byt3bl33d3r/CrackMapExec
  - https://github.com/byt3bl33d3r/CrackMapExec/wiki
---
