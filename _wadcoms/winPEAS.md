---
description: |
  winpeas.exe is a script that will search for all possible paths to escalate privileges on Windows hosts. The below command will run all priv esc checks and store the output in a file.

  Command Reference:

  	Run all checks: cmd

  	Output File: output.txt

command: |
  winpeas.exe cmd > output.txt
items:
  - Shell
OS:
  - Windows
attack_types:
  - PrivEsc
references:
  - https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/winPEAS
  - https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/blob/master/winPEAS/winPEASexe/README.md
  - https://book.hacktricks.xyz/windows/windows-local-privilege-escalation
---
