---
description: |
  PowerView is a module within PowerSploit written in PowerShell to gain network situational awareness on Windows domains. The below command will query the Domain Controller for all ASREPRoastable users.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

command: |
  Get-DomainUser -Domain test.local -DomainController 10.10.10.1 -PreauthNotRequired -Properties SamAccountName

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
