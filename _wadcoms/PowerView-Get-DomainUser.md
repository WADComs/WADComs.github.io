---
description: |
  PowerView is a module within PowerSploit written in PowerShell to gain network situational awareness on Windows domains. The below command will query the Domain Controller for all domain users.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

command: |
  Get-DomainUser -Domain test.local -DomainController 10.10.10.1
items:
  - Shell
OS:
  - Windows
attack_types:
  - Enumeration
references:
  - https://github.com/PowerShellMafia/PowerSploit/tree/master/Recon
  - https://www.attackdebris.com/?p=470
---
