import os
from Data import *
import pickle

def LoadRound():
	T = list()
	f = open('DataRound', 'r')
	contents = f.read()
	for i in contents:
		if i == '\n':
			affi(T)
			T = list()
		else:
			T.append(i)
		

	f.close()

def SaveRound(tab):
	with open('DataRound', 'a') as f:
		for i in tab:
			f.write(i)
		f.write('\n')
		f.close

def correspondence(inp):
	try:
		inp = int(inp)
	except ValueError:
		return 404

	if inp == 7  : return 0
	elif inp == 8: return 1
	elif inp == 9: return 2
	elif inp == 4: return 3
	elif inp == 5: return 4
	elif inp == 6: return 5
	elif inp == 1: return 6
	elif inp == 2: return 7
	elif inp == 3: return 8
	else: return 404

def InputCase(tab, joueur):
	while True:
		if joueur:
			case = input('Player 1 enters a case : ')
		else:
			case = input('Player 2 enters a case : ')

		case = correspondence(case)
		if case == 404:
			print("/!\ Incorrect choice. \n ")
			continue
		elif tab[case] != '-':
			print("/!\ Already taken. \n ")
			continue
		else:
			if joueur:
				tab[case] = 'X'
			else:
				tab[case] = 'O'
			break
	return tab

def affi(tab):
	print('\n' + tab[0] + tab[1] + tab[2])
	print(tab[3] + tab[4] + tab[5])
	print(tab[6] + tab[7] + tab[8])

def WinEq(tab):
	a = 0
	#analyse les case remplis du tableau
	for i in tab:
		if i != '-':
			#Une fois une case non-remplie trouveée |>
			ListMatch = LinesMatching(a)
		
			i = 0
			#Anlayse si la case trouvée correspond aux resultat de 'LinesMatching'
			while i < len(ListMatch):
				if tab[ListMatch[i][0]] == tab[ListMatch[i][1]] == tab[ListMatch[i][2]] and tab[ListMatch[i][0]] != '-':
					#si oui -> revoit True pour partie gagnée
					return True, ListMatch
				i += 1

		a += 1

def LinesMatching(pos):
	#revois les allignements possible avec un case (pos) donnée.
	LinesList = list()

	for line, case in LINES.items():
		if pos in case:
			LinesList.append(LINES[line])
	return LinesList


def Main():
	print('============= Tic tac Toe =============')
	print('\n')

	######
	tab = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
	joueur1 = True
	computer = False
	f = open('DataRound', 'w') #fichier -> vidé

	computer = input("Play against the computer? (Y)es, (N)o: ")
	if computer.upper() == 'Y':
		computer = True
		print('Computer play as player 2.')
	else:
		computer = False

	game = True
	i = 1
	
	while game:
		os.system('cls')
		affi(tab)

		if joueur1:
			tab = InputCase(tab, joueur1)
		else:
			if computer:
				tab = Computer(tab)
			else:
				tab = InputCase(tab, joueur1)
		
		if WinEq(tab):
			game = False
			if joueur1:
				os.system('cls')
				affi(tab)
				print('Player 1 win in '+str(i)+' rounds!')
			else:
				if computer:
					os.system('cls')
					affi(tab)
					print('Computer Win '+str(i)+' rounds!')
				else:
					os.system('cls')
					affi(tab)
					print('Player 2 win '+str(i)+' rounds!')
		elif '-' not in tab:
			game = False
			print('Equality')

		if game:
			if joueur1:
				joueur1 = False
			else:
				joueur1 = True

		i += 1

		SaveRound(tab)

	choice = input('\nWould you like to see the game review? (Y)es (N)o: ')
	if choice.upper() == 'Y':
		LoadRound()

	print('\n\n')
	os.system('PAUSE')
	Main()


if __name__ == '__main__':
	Main()