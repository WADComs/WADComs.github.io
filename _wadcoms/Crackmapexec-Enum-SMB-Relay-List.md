---
description: |
  "CrackMapExec (a.k.a CME) is a post-exploitation tool that helps automate assessing the security of large Active Directory networks." - https://github.com/mpgn/CrackMapExec/wiki. The following command will enumerate a list of SMB hosts with signing not enforced, allowing you to relay credentials to them using ntlmrelayx.py.

  Command Reference:

  	SMB Hosts: smb_hosts.txt

command: |
  crackmapexec smb smb_host.txt --gen-relay-list output.txt
items:
  - No_Creds
services:
  - SMB
attack_types:
  - Enumeration
OS:
  - Linux
references:
  - https://github.com/mpgn/CrackMapExec
  - https://github.com/mpgn/CrackMapExec/wiki
---
