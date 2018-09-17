from random import randrange
import pickle

def Word():
	with open("assets/Words.txt") as file:
		Words = str(file.read())
		
		ret = 0
		for i in Words:
			if i == '\n':
				ret += 1
		Words = Words.split("\n")

		return Words[randrange(ret+1)]


def Hide(Word):
	HideWord = list(Word)

	i = 0
	while i < len(Word):
		HideWord[i] = '-'
		i += 1
	
	list(Word)
	HideWord[0] = Word[0]

	return HideWord


def srch(letter, word, hide, y):
	
	word = list(word)
	for i, l in enumerate(word):
		if l == letter and y < i:
			return i
	return False


def UserScore(life):
	pseudo = input("\nEntrez votre pseudo: ")
	pseudo = pseudo.capitalize()
	DictScore = dict()

	try:
		ScoreFile = open("assets/scores", "rb")
		Pickler = pickle.Unpickler(ScoreFile)
		DictScore = Pickler.load()
		ScoreFile.close()
		try:
			DictScore[pseudo] += life
		except KeyError:
			DictScore[pseudo] = life
		ScoreFile = open("assets/scores", "wb")
		Pickler = pickle.Pickler(ScoreFile)
		print("Score total de "+str(pseudo)+': '+str(DictScore[pseudo])+".")
		Pickler.dump(DictScore)
		ScoreFile.close()

	except FileNotFoundError:
		ScoreFile = open("assets/scores", "wb")
		print("Bonjour")
		Pickler = pickle.Pickler(ScoreFile)
		DictScore[pseudo] = life
		print(DictScore)
		Pickler.dump(DictScore)
		ScoreFile.close()


def PromptScore():
	file = open("assets/scores", "rb")
	Pickler = pickle.Unpickler(file)

	Dict = Pickler.load()
	print(Dict)
	file.close()


def PromptPendu(life):
#____________
# | /	|
# |/   	O
# |    /|\ 
# |    / \
# |
#==============
	if life == 8:
		print("")
	if 8 - life == 1:
		print("\n\n\n\n\n\n")
		print("==============")
	elif 8 - life == 2:
		print("\n")
		print(" |")
		print(" |")
		print(" |")
		print(" |")
		print(" |")
		print("==============")
	elif 8 - life == 3:
		print("\n")
		print(" | /")
		print(" |/")
		print(" |")
		print(" |")
		print(" |")
		print("==============")
	elif 8 - life == 4:
		print("____________")
		print(" | /")
		print(" |/")
		print(" |")
		print(" |")
		print(" |")
		print("==============")
	elif 8 - life == 5:
		print("____________")
		print(" | /	  |")
		print(" |/       O")
		print(" | ")
		print(" | ")
		print(" |")
		print("==============")
	elif 8 - life == 6:
		print("____________")
		print(" | /	  |")
		print(" |/       O")
		print(" |        |")
		print(" |")
		print(" |")
		print("==============")
	elif 8 - life == 7:
		print("____________")
		print(" | /	  |")
		print(" |/       O")
		print(" |       /|\ ")
		print(" |  ")
		print(" |")
		print("==============")
	elif 8 - life == 8:
		print("____________")
		print(" | /	  |")
		print(" |/       O")
		print(" |       /|\ ")
		print(" |       / \ ")
		print(" |")
		print("==============")



