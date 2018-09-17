from time import time
from os import system
from math import floor

def convert(M):
	t = time()
	if type(M) == str or bytes:
		Ext = list()
		M = str(M)
		for i in M:
			Ext.append(ord(i))
	elif type(M) == list:
		Ext = str()
		Ext = ''.join(chr(i) for i in M)
	return Ext

def Uncrypt(Message, Key, LongK):
	CryptM = list()
	n = 0
	for i in Message:
		let = i - Key[n]

		while let < 32:
			let = 127+let-32
		CryptM.append(let)
		n += 1
		if n >= LongK: #creer un iterateur
			n = 0

	return CryptM

def Crypt(Message, Key, LongK):
	CryptM = list()
	n = 0
	for i in Message:
		let = i + Key[n]

		while let > 126:
			let = 32+(let-127)
		CryptM.append(let)
		n += 1
		if n >= LongK:
			n = 0

	return CryptM

def main():
	directory = input("Enter the file's directory: ")
	message = False
	if directory != '':
		with open(directory, 'r') as f:
			message = f.read()

	if message == False: message = input("Enter the message: ")
	key = input('enter the key: ')

	key = convert(key)
	t= time()
	message = convert(message)
	CryptM = Crypt(message, key, len(key))
	CryptM = convert(CryptM)
	print(CryptM)
	print('Crypt algorythm in ' + str(time() - t) + 'sec.')
	
	t = time()
	CryptM = convert(CryptM)
	CryptM = Uncrypt(CryptM, key, len(key))
	CryptM = convert(CryptM)
	print(CryptM)
	print('Uncrypt algorythm done in ' + str(time() -t) + 'sec.')

	
	if directory != '':
		f.close()



if __name__ == '__main__':
	main()

#!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
