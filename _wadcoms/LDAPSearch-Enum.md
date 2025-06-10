---
description: |
  ldapsearch is a Linux based tool that opens a connection to an LDAP server, binds, and performs a search using specified parameters. The following command will attempt to find sensitive information (such as leaked creds), by querying all LDAP objects, essentially dumping all the data that an anonymous user can access.

  Command Reference:

  	Domain: test.local

command: |
  ldapsearch -x -H ldap://test.local -D "Username@test.local" -b "DC=test,DC=local" "(sAMAccountName=Username)"
items:
  - Username
services:
  - LDAP
OS:
  - Windows
attack_types:
  - Enumeration
references:
  - https://linux.die.net/man/1/ldapsearch
---
