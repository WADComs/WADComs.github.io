---
description: |
  SharpHound.exe is the official data collector for BloodHound, written in C# and uses Windows API functions and LDAP namespace functions to collect data from domain controllers and domain-joined Windows systems. This data can then be fed into BloodHound to enumerate potential paths of privilege escalation. The following command peforms all collection methods and stores the output in a zip file that can be directly placed in the BloodHound GUI.

  Command Reference:

  	Output File: output.zip

command: |
  SharpHound.exe --CollectionMethods All --ZipFileName output.zip
items:
  - Shell
OS:
  - Windows
attack_types:
  - PrivEsc
  - Enumeration
references:
  - https://github.com/BloodHoundAD/SharpHound3
  - https://bloodhound.readthedocs.io/en/latest/data-collection/sharphound.html
---
