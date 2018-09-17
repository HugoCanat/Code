from os import system

def Listing():
	c = ''
	List = list()
	with open('Words.txt') as file:
		words = str(file.read())
		for i in words:
			if i == '\n':
				List.append(c.upper())
				c = ''
			else:
				c += i
	return List

def Search(MainList):
	Results = list()

	Search = input('\n\nEnter the letters search: ')
	Search = Search.upper()
	for i in MainList:
		if Search in i:
			Results.append(i)
		if len(Results) > 250:
			#break
			pass

	return Results

def Prompt(text):
	spaces=0
	for i in text:
		if len(i) > spaces:
			spaces = len(i)
	i = 0
	while i < len(text):
		spaces=0
		for y in text[:i+50]:
			if len(y) > spaces:
				spaces = len(y)
		a = 0
		while a < 90 and i < len(text):
			word = text[i].replace('\n', '')
			Large = spaces - len(word)
			print(word, end=(' '*(Large-3)))
			i += 1
			if i % 5 == 0 and i != 1:
				print()
			a+= 1
			
		if i < len(text):
			choice = input('\nContinue? (Y)es or not: ')
			if choice.upper() != 'Y':
				break

def Sort(text):
	c = 'AZERTYUIOPQSDFGHJKLMWXCVBN'
	instable = 'GBVHFQYXJKWZ'
	resultlist=list()
	letterList = list()
	sup = 4
	for word in text:
		score = 0
		letterList = list()
		for letter in c:
			if letter in word:# and letter not in letterList:
				if letter in instable:
					score += 2
				else:
					score +=  1
			letterList.append(letter)

		if len(word)<8 and score >= 7:
			resultlist.append(word)
		if score > 14:
			resultlist.insert(sup, word)
			sup += 5

	return resultlist

def Main():
	#system('mode con cols=85 lines=38')
	print('BombParty Cheat 1.0')
	print('\n' + 'Loading the list of words..')
	sort = input('Put Y to sort results : ')
	sort = sort.upper()
	MainList = Listing()
	print(str(len(MainList)) + ' words Loaded.')

	choice = 'Y'
	while choice == 'Y' or choice == '\n':
		results = Search(MainList)
		if sort == 'Y':
			SortResults = Sort(results)
			print(str(len(SortResults)) + ' sorted results find, '+str(len(results)) + ' normal results find.')
			Prompt(SortResults)
		else:
			print(str(len(results)) + ' results find.')
			Prompt(results)




	



if __name__ == '__main__':
	Main()