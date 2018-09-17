from math import sqrt
def main():
	print("=== Polynome du second degré ===")
	a = int(input('Valeur a: '))
	b = int(input('Valeur b: '))
	c = int(input('Valeur c: '))

	delta = (b*b)-(4*a*c)
	print('Valeur du discriminant :' + str(delta))

	if delta == 0:
		x = (-b)/2*a
		print("L'unique soluion est: "+ str(x))

	if delta > 0:
		x1 = ((-b)+sqrt(delta))/(2*a)
		x2 = ((-b)-sqrt(delta))/(2*a)
		print("Les deux solutions sont :" + str(x1) +" et " + str(x2))



if __name__ == "__main__":
	main()