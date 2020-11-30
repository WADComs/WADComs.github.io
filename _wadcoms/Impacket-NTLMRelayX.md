---
description: |
  Impacket's ntlmrelayx.py performs NTLM Relay Attacks, creating an SMB and HTTP server and relaying credentials to various different protocols (SMB, HTTP, LDAP, etc.).

  The below command creates an SMB relay server that targets the IP 10.10.10.1, meaning any credentials that the SMB server recieves, gets relayed to that IP to attempt to authenticate and execute 'whoami /all'. In order for the SMB server to recieve credentials to relay, dementor.py can be used to trigger a forced authentication from the IP it's targeting to an attacker controlled SMB server.

  Command Reference:

  	Target IP: 10.10.10.1

items:
  No_Creds:
    - code: |
        python3 ntlmrelayx.py -smb2support -t smb://10.10.10.1 -c 'whoami /all' -debug
filters:
  Linux:
    - code: |
        empty
  Windows:
    - code: |
        empty
---
