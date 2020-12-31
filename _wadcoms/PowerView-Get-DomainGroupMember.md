---
description: |
  PowerView is a module within PowerSploit written in PowerShell to gain network situational awareness on Windows domains. The below command will query the Domain Controller for a list of members of the Domain Admins group.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Group: Domain Admins

command: |
  Get-DomainGroupMember -identity "Domain Admins" -Domain test.local -DomainController 10.10.10.1
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
