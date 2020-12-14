---
description: |
  SharpWMI.exe is part of the GhostPack suite of tools that provides WMI functionality, such as local/remote WMI queries, remote WMI process creation, and remote execution of arbitrary VBS through WMI events. The following command will simply list all processes running on the local system.

  Command Reference:

  	Get all processes: "select * from win32_process"

command: |
  SharpWMI.exe action=query query="select * from win32_process"
items:
  - Shell
services:
  - WMI
OS:
  - Windows
attack_types:
  - Persistence
references:
  - https://github.com/GhostPack/SharpWMI
  - https://www.harmj0y.net/blog/redteaming/ghostpack/
---
