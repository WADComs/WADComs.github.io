---
description: |
  "CrackMapExec (a.k.a CME) is a post-exploitation tool that helps automate assessing the security of large Active Directory networks." - https://github.com/byt3bl33d3r/CrackMapExec/wiki

  Command Reference:

<<<<<<< HEAD
  	Target IP: 10.10.10.1

  	Username: john

  	Password: password123
=======
    Target IP: 10.10.10.1
    
    Username: john
    
    Password: password123
>>>>>>> 3842148fab26eb80963d666a41840752e9b34299

command: |
  crackmapexec smb 10.10.10.1 -u 'john' -p 'password123' --shares
items:
  - Username
  - Password
services:
  - SMB
attack_types:
  - Enumeration
OS:
  - Linux
references:
  - https://github.com/byt3bl33d3r/CrackMapExec
  - https://github.com/byt3bl33d3r/CrackMapExec/wiki
---
