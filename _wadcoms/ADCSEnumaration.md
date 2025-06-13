---

description: |
  Active Directory Certifcate Services or ADCS provide an alternative way to authenticate within a AD enviroment that contains a PKI as well as 
  being configured with a Certifcate Authority. References below will provide technical info on ADCS as well as exploitation techniques from 
  spectorops certfied preowned white paper.

command: |
  #Note that we are just enumarating here. We are not preforming exploitation. There is a linux equalivent called certipy that works much the same way
  # Find CAs 
  C:Tools\Certify.exe cas 

  # Find templates
  C:Tools\Certify.exe find 

  # Find vulnerable templates
  C:Tools\Certify.exe find /vulnerable 


items:
  - Shell
OS:
  - Windows
attack_types:
  - Enumeration
references:
  - https://github.com/GhostPack/Certify
  - https://posts.specterops.io/certified-pre-owned-d95910965cd2
  - https://www.thehacker.recipes/ad/movement/adcs/