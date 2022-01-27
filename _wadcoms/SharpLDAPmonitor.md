---
description: |
  SharpLDAPmonitor.exe allows you to monitor creation, deletion and changes to LDAP objects live during your pentest.

  Command Reference:

  	Target IP: 10.10.10.1

  	Attacker IP: 10.10.10.2

  	Domain: test.local

  	Username: john

  	Password: password123

command: |
  SharpLDAPmonitor.exe /dcip:10.10.10.1 /user:TEST.local\john /pass:password123

items:
  - Password
  - Username
services:
  - LDAP
  - Kerberos
  - NTLM
OS:
  - Windows
attack_types:
  - Enumeration
references:
  - https://github.com/p0dalirius/LDAPmonitor/tree/master/csharp
---
