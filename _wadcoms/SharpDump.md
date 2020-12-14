---
description: |
  SharpDump.exe is part of the GhostPack suite of tools and is a C# port of PowerSploit's Out-Minidump.ps1. It can dump the process for LSASS or a specific process given it's PID. This dump can then be fed into mimikatz to extract sensitive information. The following command simply dumps the LSASS process.

command: |
  SharpDump.exe
items:
  - Shell
OS:
  - Windows
attack_types:
  - PrivEsc
  - Enumeration
references:
  - https://github.com/GhostPack/SharpDump
  - https://www.harmj0y.net/blog/redteaming/ghostpack/
---
