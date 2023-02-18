import os
import sys
from cryptography.fernet import Fernet
import glob

def d():
#			v		EDIT NAME OF KEY HERE v
	name = 'MASTER.key'
	with open(name, 'rb') as filekey:
		key = filekey.read()

	fernet = Fernet(key)
	executable_files = glob.glob('*.exe') + glob.glob('*.exew')
	for file in executable_files:
		with open(file, 'rb') as enc:
			encrypted = enc.read()
	decrypted = fernet.decrypt(encrypted)
	for file in executable_files:
		with open(file, 'wb') as dec:
			dec.write(decrypted)

	print(' [+]  ALL EXE FILES HAVE BEEN DECRYPTED  [+]')
	print('\n \n \n					[! ! ! ! !]\n \n			DO  NOT  DELETE  THE  KEY\n	DO NOT DELETE THE DECRYPTOR FILE  \n \n 	EVER')

d()
