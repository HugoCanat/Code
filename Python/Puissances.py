"""Programme chargé de déterminer la puissance à laquelle est un nombre (entier)
 grace au résultat de cette puissance"""

def main():
	while True:
		try:
			number = int(input('Enter the number: '))
			result = int(input('Enter the result: '))
		except ValueError:
			print('/!\ Error invalid value.\n')
			continue
		break

	print('Searching the pow..')
	i = 0
	while True:
		if number**i == result:
			break
		i += 1

	print('The pow is : '+ str(i))

if __name__ =='__main__':
	main()