---
description: Enumerate RPC services on a remote Windows machine using Impacket's rpcdump with NTLM Pass-the-Hash.

Command Reference:
    Target IP: 10.10.10.1
    Domain: test.local
    Username: john
    Hash: 580B16D486D8D2CAFA00B314D41FA396 (NTLM hash)

command: |
  impacket-rpcdump -hashes 00000000000000000000000000000000:580B16D486D8D2CAFA00B314D41FA396 test.local/john@10.10.10.1

items:
  - Hash
  - Enumeration

services:
  - RPC
  - NTLM

OS:
  - Windows

attack_types:
  - Pass-the-Hash
  - Enumeration

references:
  - https://github.com/fortra/impacket
---
