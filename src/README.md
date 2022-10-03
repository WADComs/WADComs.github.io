# WADComs in Terminal

This is a terminal-based tool that allows users to search for tools and commands without going to the website.

This is a work in progress.

### Usage
```bash
usage: wadcoms.py [-h] [-H HAVE [HAVE ...]] [-T TYPE [TYPE ...]] [-S SERVICES [SERVICES ...]] [-O OS [OS ...]] [-i]

Terminal-based tool to access @JohnWoodman15's https://wadcoms.github.io/

options:
  -h, --help            show this help message and exit
  -H HAVE [HAVE ...], --have HAVE [HAVE ...]
                        What you have. Options are: {Username, Password, No Creds, Hash, TGS, TGT, PFX, Shell}
  -T TYPE [TYPE ...], --type TYPE [TYPE ...]
                        Attack Type Options are: {Enumeration, Exploitation, Persistence, Privilege Escalation}
  -S SERVICES [SERVICES ...], --services SERVICES [SERVICES ...]
                        Services. Options are: {SMB, WMI, DCOM, Kerberos, RPC, LDAP, NTLM}
  -O OS [OS ...], --os OS [OS ...]
                        Operating System. Options are: {Linux, Windows}
  -i, --interactive
```
