import os

key = 'R50Uqays81BEKlD6rcu8Rf696m38lbdaFGr09Ro04K3sWX9pJ6c4QcBLc25RnoYefCE6L464a09EgjS5Skgn404OlLuBx5Q2W8l3685T0EIoPP6ZP3Tz71L7Zlv5457d5C04Dpmb86lFH21WcX0X8ka5gXFqajvRH91hcs0JWqeTzn07pcVl5aHy2o6f6lYGDx14Iy149'

def convert(M):
	if type(M) == str or type(M) == bytes:
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
	if directory == '\n' or directory == '': directory = 'assets\VanillaPhoto.jpg'
	print(directory)
	global key
	key = convert(key)
	try:
		F = open(directory, 'rb')
		Data = F.read()
		print(Data[:20])
		Data = Data.decode('utf-8')
		print(Data[:20])
		CryptedData = convert(Data)
		print('File converted.')
		CryptedData = Crypt(CryptedData, key, len(key))
		print('File crypted.')
		CryptedData = convert(CryptedData)
		print('Done')
		f = open('assets\PhtoCrypt.jpg', 'w')
		f.write(CryptedData)

		F = open('assets\PhtoCrypt.jpg', 'r')
		Data = F.read()
		CryptedData = convert(Data)
		print('convert')
		CryptedData = Uncrypt(CryptedData, key, len(key))
		print('uncrypt')
		CryptedData = convert(CryptedData)
		print('Done.')
		f = open('assets\PhtoUcrypt.jpg', 'wb')
		CryptedData = str.encode(CryptedData)
		print(type(CryptedData))
		print(CryptedData[:20])
		f.write(CryptedData)

		F.close()
		f.close

	except FileNotFoundError:
		print('Error File Not Found, retry')
		main()

if __name__ == "__main__":
	main()