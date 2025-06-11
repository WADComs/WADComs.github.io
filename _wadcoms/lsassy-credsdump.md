---

description: |
    "lsassy is a tool written in python released in 2021 to provide a varity of methods to dump credintials from a single/multiple remote targets. It uses a varity of differnt tactics that provide OPSEC benefits in some cases while also providing the operator options in how it executes remotely, which method it uses as well as the ability to replace the inbuild binaries with your own very easily. Note that if you had introduced nxc into the enviroment previously, then youre encouraged for OSPEC gains to use the built in lsass module. This holds true for many sources in this project that if you had introduced x y z tool; you are better off continuing to use those instead of constantly introducing new ones"

    Command reference:
        Password: password123
        Username: john
        Domain: test.local
        Target: 10.10.10.1
command: |
    lsassy -u john -p password123 -d test.local 10.10.10.1
items:
  - Username
  - Password
services:
  - Kerberos
  - NTLM
OS:
  - Linux
attack_types:
  - Exploitation

references:
  - https://en.hackndo.com/remote-lsass-dump-passwords/
  - https://github.com/login-securite/lsassy?tab=readme-ov-file
---

