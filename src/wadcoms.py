#!/bin/python3

import os
from pathlib import Path
import argparse
import pickle
from pprint import pprint
import yaml
import shutil


def loadFiles():
	tools = []
	# If we already have the tools loaded into memory, deserealize them
	if(os.path.exists('./wadObj')):
		with open('./wadObj', 'rb') as fin:
			tools = pickle.load(fin)

	else:
		os.makedirs('temp')

		# make copies of files to fix them
		for path in Path('../_wadcoms').rglob('*.md'):
			with open(path, 'rb') as fin:
				fileContents = fin.readlines()


			# remove end formatting
			while b'---' in fileContents[-1]:
				del fileContents[-1]

			with open(f'temp/{path.stem}.yaml', 'wb') as fout:
				fout.write(b'\n'.join(fileContents))

		# read yaml files
		for path in Path('temp').rglob('*.yaml'):
			with open(path, 'rb') as fin:
				try:
					tools.append(yaml.safe_load(fin))
				except yaml.YAMLError as exc:
					print(exc)
		shutil.rmtree('temp')

		# pickle loaded files

		with open('wadObj', 'wb') as fout:
			pickle.dump(tools, fout, pickle.HIGHEST_PROTOCOL)
	

	return tools



'''
Initialize parser
'''

parser = argparse.ArgumentParser(description='Terminal-based tool to access @JohnWoodman15\'s https://wadcoms.github.io/')
parser.add_argument('-H', '--have', nargs='+', default=[], help='What you have.\nOptions are: {Username, Password, No Creds, Hash, TGS, TGT, PFX, Shell}')
parser.add_argument('-T', '--type', nargs='+',  default=[], help='Attack Type\nOptions are: {Enumeration, Exploitation, Persistence, Privilege Escalation}')
parser.add_argument('-S', '--services', nargs='+',  default=[], help='Services.\nOptions are: {SMB, WMI, DCOM, Kerberos, RPC, LDAP, NTLM}')
parser.add_argument('-O', '--os', nargs='+',  default=[], help='Operating System.\nOptions are: {Linux, Windows}')

parser.add_argument('-i', '--interactive', default=False, action='store_true')

args = parser.parse_args()
tools = loadFiles()
print(f'[*] {len(tools)} tools loaded')

'''
TODO: Make Interactive Mode
'''
if args.interactive:
	print("[*] Starting Interactive Mode:")


	exit()

'''
Filter unwanted tools
'''


# Filter OS
for i in range(len(tools)-1, -1, -1):
	if len(args.os) == 0:
		break

	toolOS = tools[i]['OS']
	requestedOS = args.os


	if set(requestedOS) > set(toolOS):
		del tools[i]

# Filter Have
for i in range(len(tools)-1, -1, -1):
	if len(args.have) == 0:
		break

	toolHave = tools[i]['items']
	requestedHave = args.have


	if set(requestedHave) != set(toolHave):
		del tools[i]

# Filter Services
for i in range(len(tools)-1, -1, -1):
	if len(args.services) == 0:
		break

	toolServices = tools[i]['services']
	requestedServices = args.services


	if set(requestedServices) != set(toolServices):
		del tools[i]

# Filter type
for i in range(len(tools)-1, -1, -1):
	if len(args.type) == 0:
		break

	toolType = tools[i]['attack_types']
	requestedType = args.type


	if set(requestedType) != set(toolType):
		del tools[i]


print(f"[*] Found {len(tools)} matching tools:\n")

sstring = '-'*int(os.get_terminal_size().columns)

for i in tools:
	print('Description:')
	print(i['description'])
	print('\nCommand Reference:')
	print(i['command'])
	print('\nReferences:')
	print("\n".join(i['references']))
	print(sstring)