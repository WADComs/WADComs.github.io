---
description: |
  Responder is an LLMNR, NBT-NS, and MDNS poisoner. It will answer to specific NBT-NS (NetBIOS Name Service) queries based on their name suffix. By default, the tool will only answer to File Server Service request, which is for SMB. The following command will put Responder in analyze mode, listening for NBT-NS, BROWSER, and LLMNR requests without responding.

  Command Reference:

  	Interface: eth0

command: |
  Responder -I eth0 -A
items:
  - No_Creds
services:
  - NTLM
  - SMB
OS:
  - Linux
  - Windows
attack_types:
  - Exploitation
references:
  - https://github.com/lgandx/Responder
  - https://www.ivoidwarranties.tech/posts/pentesting-tuts/responder/cheatsheet/
---
