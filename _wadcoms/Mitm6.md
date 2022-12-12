---
description: |
  mitm6 is a pentesting tool that exploits the default configuration of Windows to take over the default DNS server. It does this by replying to DHCPv6 messages, providing victims with a link-local IPv6 address and setting the attackers host as default DNS server. The following command will respond to DHCPv6 messages and set the DNS server to the attack host IP. Leverage this command with ntlmrelayx.py to capture the WPAD configuration requests. 

  Command Reference:

  	Domain: test.local

command: |
  mitm6 -d test.local --ignore-nofqnd
items:
  - No_Creds
services:
  - DNS
OS:
  - Linux
  - Windows
attack_types:
  - Exploitation
references:
  - https://github.com/dirkjanm/mitm6
  - https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/
---
