from random import *
from os import system
import sys
import getopt
def RandPass(Length, maj=True, minu=True, num=True):
	
	PasswordLength = Length
	#1->A-Z, 2->a-z, 3->0-10
	password = ''	

	while len(password) <= PasswordLength:
		rand = randrange(1000)%3
		if rand == 0 and maj:
			password += chr(65 + randrange(1000)%26)
		if rand == 1 and minu:
			password += chr(97 + randrange(1000)%26) 
		if rand == 2 and num:
			password += chr(48 + randrange(1000)%10)

		
	return password

def Main():
	Run = ''

	"""Run = input('(S)ettings or (R)un: ')
	if Run.upper() == 'O':
		print('[+] Settings [+]')
		print('(U)ppercase = ' +str(maj))
		print('(L)owerCase = ' + str(minu))
		print('(N)umber = ' + str(num))
		print()
		choix = input('What you want to change?(put the corresponding letter(s)\n')
		if 'U' in choix.upper():
			if maj:
				maj = False
			else:
				maj = True
		if 'L' in choix.upper():
			if minu:
				minu = False
			else:
				minu = True
		if 'N' in choix.upper():
			if num:
				num = False
			else:
				num = True
		print()
		print('[+] New settings[+]')
		print('(U)ppercase = ' +str(maj))
		print('(L)owerCase = ' + str(minu))
		print('(N)umber = ' + str(num))"""

	maj = True
	minu =True
	num = True

	print(sys.argv)
	if len(sys.argv) > 1:
		maj = False
		minu =False
		num = False
		for o in sys.argv[1:]:
			if 'u' in o:
				maj = True
			if 'l' in o:
				minu = True
			if 'n' in o:
				num = True
	else:
		maj = True
		minu =True
		num = True


	File = input('Save the key, Y/N : ')
	if File.upper() == 'Y':
		directory = input("Enter the file's directory: ")
		try:
			f = open(directory, 'w')
		except FileNotFoundError:
			E = True
			print('Error file not found.\n')
			while E:
				E = input('Retry, or (E)xit: ')
				if E.upper != 'E':
					with open(directory, 'w') as f:
						pass



	PasswordLength = input('Password length: ')
	PasswordLength = int(PasswordLength)

	password = RandPass(PasswordLength, maj, minu, num)	
	print('Done.')
	if File.upper() == 'Y':
		f.write(password)
	else:
		print(password)




if __name__ == '__main__':
	Main()
