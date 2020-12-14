---
description: |
  Impacket's atexec.py uses the Task Scheduler service on the remote Windows host to execute the given command. It will create a windows task with a random name, trigger the task, and then delete it. The following command executes `whoami` on the remote Windows host.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

  	Command Executed: whoami
command: |
  python3 atexec.py test.local/john:password123@10.10.10.1 whoami
items:
  - Password
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
