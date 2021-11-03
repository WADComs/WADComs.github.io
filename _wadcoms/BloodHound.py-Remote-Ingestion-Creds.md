---
description: |
  BloodHound is a single page Javascript web application, built on top of Linkurious, compiled with Electron, with a Neo4j database fed by a data collector. BloodHound uses graph theory to reveal the hidden and often unintended relationships within an Active Directory environment. Attackers can use BloodHound to easily identify highly complex attack paths that would otherwise be impossible to quickly identify. Defenders can use BloodHound to identify and eliminate those same attack paths. Both blue and red teams can use BloodHound to easily gain a deeper understanding of privilege relationships in an Active Directory environment.

  BloodHound.py is a Python based ingestor for BloodHound, based on Impacket. It allows you to remotely collect data for bloodhound by querying LDAP

  Command Reference:

  	Target IP: 10.10.10.1

  	Username: john

  	Password: password123

  	Domain: test.local

command: |
  bloodhound.py -u john -p password123 -d test.local -v --zip -c All -dc test.local -ns 10.10.10.1
items:
  - Username
  - Password
services:
  - LDAP
attack_types:
  - Enumeration
OS:
  - Linux
  - Windows
references:
  - https://github.com/BloodHoundAD/BloodHound
  - https://github.com/fox-it/BloodHound.py
---
