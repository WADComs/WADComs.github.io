---
description: |
  Nmap's `krb5-enum-users` script attempts to bruteforce and enumerate valid Active Directory accounts through Kerberos Pre-Authentication. The following command will attempt to enumerate valid usernames given a list of usernames to try.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username List: usernames.txt
command: |
  nmap -p 88 --script=krb5-enum-users --script-args krb5-enum-users.realm='test.local',userdb=usernames.txt 10.10.10.1
items:
  - No_Creds
services:
  - Kerberos
  - Enumeration
OS:
  - Linux
  - Windows
attack_types:
  - Enumeration
references:
  - https://nmap.org/download.html
  - https://nmap.org/nsedoc/scripts/krb5-enum-users.html
---
