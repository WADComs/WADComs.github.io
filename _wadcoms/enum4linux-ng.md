---
description: |
  enum4linux-ng is a modern reimplementation of enum4linux written in Python3. It is used to enumerate information from Windows and Samba systems, providing cleaner output and better support for modern protocols. The following command performs a full unauthenticated enumeration of the target.

  Command Reference:

  	Target IP: 10.10.10.1

command: |
  enum4linux-ng 10.10.10.1
items:
  - No_Creds
services:
  - SMB
OS:
  - Linux
attack_types:
  - Enumeration
references:
  - https://github.com/cddmp/enum4linux-ng
---
