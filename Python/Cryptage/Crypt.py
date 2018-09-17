from os import system
from time import time

def Uncrypt(crypt, key):

	decrypt = ''
	k = 0
	i = 0

	while i < len(crypt):
		decrypt += chr( ((ord(crypt[i])-32)+95) - (ord(key[k])-32)+32 )
		#print(ord(decrypt[i]))

		while ord(decrypt[i]) > 126:
			decrypt = decrypt[:i] + chr(ord(decrypt[i]) - 95) + decrypt[i+1:]
		i += 1
		k += 1

		if k > len(key)-1:
			k = 0
	return(decrypt)


def Crypt(message, key):
	#Old -> message = input("\nEnter your text: \n")

	ConvertMessage = ""
	for l in message:
		if l == 'é' or l == 'è' or l == 'ê' or l == 'ë':
			l = 'e'
		elif l == 'É':
			l = 'E'
		elif l == 'à':
			l = 'a'
		elif l == 'ï' or l == 'ì' or l == 'î':
			l = 'i'

		ConvertMessage += l

	message = ConvertMessage

	#Old -> key = input('\nEnter the key: \n')
	
	crypt = ""
	i = 0
	k=0

	while i < len(message):
		crypt += chr((((ord(message[i])-32) + (ord(key[k])-32))%95)+32)
		#print(ord(crypt[i]))

		i += 1
		k += 1
		if k > len(key)-1:
			k = 0
	return(crypt)

def main():
	choice = input('(C)rypt, (U)ncrypt or (F)ile: ')
	
	if choice.upper() == 'U':
		crypt = input('\nEnter the crypted message: \n')
		key = input('\nEnter the key: \n')
		print('\nUncrypted Message: \n' + Uncrypt(crypt, key))
	
	elif choice.upper() == 'C':
		message = input("\nEnter your text: \n")
		key = input('\nEnter the key: \n')
		print('\nCrypted Message: \n' + Crypt(message, key))
	else:
		Dir = input("Enter the file's directory: ")
		with open(Dir, 'r') as file:
			message = file.read()
			print('File open.')
		cu = input('(C)rypt or (U)ncrypt: ')
		if cu.upper() == 'C':
			key = input('\nEnter the key: \n')
			t = time()
			CryptedM = Crypt(message, key)
			t = time() - t
			print('Done in ' + str(t) + ' sec.')
		else:
			key = input('\nEnter the key: \n')
			t = time()
			CryptedM = Uncrypt(message, key)
			t = time() - t
			print('Done in ' + str(t) + ' sec.')
		continu = input('Continue? Y/N: ')
		if continu.upper() == 'Y':
			print('\nCrypted Message: \n' + CryptedM)



if __name__ == "__main__":
		main()