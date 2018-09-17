import time
from os import system

def Add(Number):
	"""s'occupe de retourner les cases additionée"""
	Number[8] += 1
	b = 1

	for i,a in enumerate(Number):
			if a > 9:	
				Number[i-1] += 1	
				while Number[i-b] > 9:
					Number[i-b] = 1
					Number[i-b-1] += 1
					b += 1

				Number[i] = 1
				b = 1
	return Number

def Layer(number, changeables_cases):
	layer = 0
	#-> couches de calculs: nombre de cases a émulées 
	#initialisé a 0 pour eviter tout bug avec les instructions suivantes
	for a in changeables_cases:
		#si une case changeable est différente de 0 alors elle a été changée
		#donc layer += 1
		if number[a] != 0:
			layer += 1
	#il ne peut y avoir 0 couches de calculs, donc par defaut layer = 1
	if layer == 0: layer += 1
	return layer

def NextN(number, Number):
	base = [1,2,3,4,5,6,7,8,9]
	free = sorted([i for i in base if i not in Number])

	for i in free:
		if i > number:
			break

	return i


def NextRound(Number, last_number):
	base = [1,2,3,4,5,6,7,8,9]
	free = sorted([i for i in base if i not in Number])
	changeables_cases = [i for i,a in enumerate(Number) if a is 0]
	
	layer = Layer(last_number, changeables_cases)
	#######################################

	#changeables_cases[layer-1] -> revient a la case changeable correspondante a la couche atuelle
	#plus la couche est élévée plus on interferera avec des cases(changeables) élévées

	next_number = list(last_number)

	ActualLayer = layer
	#Si si la derniere couche ne peut plus etre augementé car elle a deja la valeur maximum dispo
	if next_number[changeables_cases[ActualLayer-1]] >= free[len(free)-1]:
		#On met celle ci a 0
		next_number[changeables_cases[ActualLayer-1]] = 0
		#Pour s'occuper de la couche précédente s'il en existe une, et l'augmenté
		if layer > 1:
			next_number[changeables_cases[ActualLayer-2]] = NextN(next_number[changeables_cases[ActualLayer-2]], next_number)
		#Et seulement ensuite on s'occuper de la couche de base
		next_number[changeables_cases[ActualLayer-1]] = NextN(next_number[changeables_cases[ActualLayer-1]], next_number)
	else:
		next_number[changeables_cases[layer-1]] = NextN(next_number[changeables_cases[layer-1]], next_number)
	
	print(layer)

	return next_number
	



def stable(Number):
	same_number = list()
	for indice,nombre in enumerate(reversed(Number)):
		if nombre in Number[:8-indice] or nombre in Number[8-(indice-1):]:
			if nombre not in same_number:
				same_number.append(nombre)
	print('Iteration of number : ' + str(same_number))


def Main(Tab = ['-'] * 9):

	EmptyCase = [i for i,a in enumerate(Tab) if a == '-']
	Player = 'X'
	PlayerCases = list()
	Player2 = 'O'
	Player2Cases = list()

	Number = [1, 2, 3, 4, 0, 0, 0, 0, 0]
	base = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	Iterations = 0
	#free = sorted([i for i in d if i not in Number])
	
	next_number = list(Number)
	while Number[0] <= 9:
		Iterations += 1

		#Number = Add(Number)
		next_number = NextRound(Number, next_number)
		print(next_number)
		input('')
		#stable(Number)

if __name__ == '__main__':
	Main()

