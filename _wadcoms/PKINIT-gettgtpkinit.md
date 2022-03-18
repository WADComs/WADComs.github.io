---
description: |
  PKINIT gettgtpkinit.py request a TGT using a PFX file, either as file or as base64 encoded blob, or PEM files for cert+key. This uses Kerberos PKINIT and will output a TGT into the specified ccache. It will also print the AS-REP encryption key which you may need for the getnthash.py tool.

  Command Reference:

    Domain: test.local

    Host that you got the certificate from: DC01

    PFX file: crt.pfx

    PFX file password: password123

    TGT requested: out.ccache

command: |
  python3 gettgtpkinit.py test.local/DC01\$ -cert-pfx crt.pfx -pfx-pass password123 out.ccache
items:
  - Username
  - Password
  - PFX
services:
  - Kerberos
OS:
  - Linux
  - Windows
attack_types:
  - Exploitation
  - PrivEsc
references:
  - https://github.com/dirkjanm/PKINITtools
  - https://dirkjanm.io/ntlm-relaying-to-ad-certificate-services/
---
