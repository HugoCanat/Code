from Fonct import *
import os
import pickle

def main():
	life = 8
	print("  --Bienvenue dans ce jeu du Pendu!--")
	input("Appuyez sur une touche pour commencer.")

	SecretWord = str(Word())
	HideWord = Hide(SecretWord)
	UseLetter = ""

	letter = 'abc'
	while HideWord != list(SecretWord):
		os.system("cls")
		
		print("\n" + "".join(HideWord))
		print("Vous avez " + str(life) + " vies.")
		PromptPendu(life)
		if life == 0:
			break

		if UseLetter != "":
			print("Lettres fausses: " + UseLetter)

		letter = input("Entrez une lettre: ")
		while len(letter) > 1 or letter == "" or letter.upper() in UseLetter:
			if letter.upper() in UseLetter:
				print("/!\ Vous avez déja essayé cette lettre.")
			else:
				print("/!\ N'entrez seulement qu'une lettre.\n")
			letter = input("Entrez une lettre: ")
		letter = letter.upper()

		var = 0
		if srch(letter, SecretWord, HideWord, var) == False:
			print("/!\ Cette lettre n'est pas dans le mot.\n")
			UseLetter += letter + " - "
			life -= 1
		else:
			while srch(letter, SecretWord, HideWord, var) != False:
				var = srch(letter, SecretWord, HideWord, var)
				HideWord[var] = letter


	if life == 0:
		print("\n/!\ Vous avez perdu.")
		print("Le mot était: " + SecretWord + ".")
		UserScore(life)
	else:
		print("\nVous avez gagné!")
		print("Le mot était: "+ SecretWord +".")
		UserScore(life)
	choix = input("Afficher les scores generaux? (O/N):")
	choix = choix.upper()
	if choix == 'O':
		PromptScore()



	os.system("PAUSE")

if __name__ == "__main__":
	main()