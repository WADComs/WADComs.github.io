---
description: |
  Rubeus' `asreproast` module will attempt to harvest the non-preauth AS_REP responses for a given list of usernames. These responses will be encrypted with the user's password, which can then be cracked offline. The following command is run on a Windows machine in the victim domain.

  Command Reference:

  	Output File: hashes.txt

command: |
  Rubeus.exe asreproast /format:hashcat /outfile:hashes.txt
items:
  - Shell
services:
  - Kerberos
OS:
  - Windows
attack_types:
  - Exploitation
  - PrivEsc
references:
  - https://github.com/GhostPack/Rubeus
  - https://github.com/GhostPack/Rubeus#asreproast
---
