---
description: |
  Evil-WinRM uses the Windows Management Instrumentation (WMI) to give you an interactive shell on the Windows host. Winrm Supports PKINIT, meaning if you have a computers PFX file, you can authenticate and get a shell. Note that the command requires a public and a private key in PEM format, that can be extracted by converting the PFX to PEM format. Take a look at the references for more info on that. Password protected PFX files can be cracked with JohnTheRipper.

  Command Reference:

  	Target IP: 10.10.10.1

  	PFX File: cert.pfx

  	Domain: EVILCORP

command: |
  evil-winrm -i 10.10.10.1 -c pub.pem -k priv.pem -S -r EVILCORP
items:
  - PFX
services:
  - WMI
OS:
  - Windows
attack_types:
  - Exploitation
references:
  - https://github.com/Hackplayers/evil-winrm
  - https://book.hacktricks.xyz/cryptography/certificates
---
