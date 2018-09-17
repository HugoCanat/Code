#jeu de casino #
from math import *
import random
import os

partie = True
bien = 100
somme_misee = 0
caseJ = 100
caseR = 0

bien = int(bien)
somme_misee = int(somme_misee)

print(" -___--ZCasino--___- \n\n")

while partie:
    print ("vous possedez :", bien, "$.")
    caseJ = 100
    while caseJ < 0 or caseJ > 49:
        caseJ = input("Entrer la case sur laquel vous voulez miser (entre 0 et 49):")

        try :
            caseJ = int(caseJ)

        except ValueError:
            print ("Ce n'est pas un nombre.")
            caseJ = -1
            continue

        if caseJ < 0 or caseJ > 49:
            print ("Case choisie incorrect.")

    somme_misee = -1
    while somme_misee > bien or somme_misee < 1:
        somme_misee = input("Entrer le montant de votre mise:")

        try:
            somme_misee = int(somme_misee)
        except ValueError:
            print ("Ce n'est pas un nombre.")
            somme_misee = -1
            continue

        if somme_misee > bien:
            print ("Montant trop eleve par rapport a vos biens.")
        elif somme_misee < 1:
            print ("Montant trop faible.")

    caseR = random.randrange(50)
    print (caseR)

    if caseJ == caseR:
        print ("Vous avez gagner! \n")
        bien += 3*somme_misee
    elif (caseJ%2) == (caseR%2):
        print ("Vous gagner le moitier de votre mise (numero de meme couleur).\n")
        bien += ceil(somme_misee/2)
    else:
        print ("Perdu.\n")
        bien -= somme_misee

    if bien == 0:
        print ("Vous n'avez plus d'agent, vous avez perdu.")
        break
    choix = input ("")

os.system("PAUSE")
