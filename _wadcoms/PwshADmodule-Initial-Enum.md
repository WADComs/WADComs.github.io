---
description: |
  These commands provide a quick refernece for using the AD module to get situational awerness of the AD environment.
  Note that to get more commands that you can run, use the get command cmdlet, e.g. `Get-Command -Module ActiveDirectory` But Thes
  are the standard commands that will get you standard. Feel free to replace the first pipe with the -server "your domain" if you dont want
  to enumarate the entire forest. For more info on using the AD module, please check out our discussion on the AD module in WADCOMs.

command: |
  #Getting all DCs in the forest
  (Get-ADForest).Domains | % { Get-ADDomainController -DomainName $_ -Discover }

  #Getting all users in the forest
  (Get-ADForest).Domains | % { Get-ADUser -Filter * -Server $_ }

  #Getting all computers in the forest
  (Get-ADForest).Domains | % { Get-ADComputer -Filter * -Server $_ }

  #Mapping out entire trust relationships
  Get-ADTrust -Filter '(intraForest -ne $True) -and (ForestTransitive -ne $True)' | Select-Object Source,Target,Name

  #Getting all groups in a domain. Note that the select statement will limit the output to only the matching fields the object contains
  Get-ADGroup -Filter * | Select-Object SamAccountName, GroupScope, DistinguishedName

OS:
  - Windows
attack_types:
  - Enumeration
references:
  - https://docs.microsoft.com/en-us/powershell/module/activedirectory/
  - https://github.com/samratashok/ADModule
---