---
description: |
  ldapsearch is a Linux based tool that opens a connection to an LDAP server, binds, and performs a search using specified parameters. The following command will attempt to find sensitive information (such as leaked creds), by querying all LDAP objects, essentially dumping all the data that an anonymous user can access.

  Command Reference:

  	Domain: test.local
    
  	Username: ldap
    
  	Password: password123

command: |
  ldapsearch -h test.local -D 'ldap@test.local' -w password123 -b 'dc=test,dc=local'
items:
  - Username
  - Password
services:
  - LDAP
OS:
  - Linux
attack_types:
  - Enumeration
references:
  - https://linux.die.net/man/1/ldapsearch
---
