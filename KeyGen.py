from cryptography.fernet import Fernet
import os
import sys

def gen():
	r_name = input('Whats Would You Like To Be The Title Of Your Key:\n> ')
	name = r_name + '.key'
	key = Fernet.generate_key()
	with open(name, 'wb') as filekey:
		filekey.write(key)



gen()
