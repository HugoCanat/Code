# -*-coding:Latin-1 -*
#generateur d'années bissextiles.

import os
"""Bonjour, voici un programme qui calcul les annees bissextiles
jusqu'a une annee demander"""
nombre = input("saisissez une annee:")
try:

    nombre = int(nombre) # On tente de convertir l'année

    if nombre<=0:

        raise ValueError("l'année saisie est négative ou nulle")

except ValueError:

    print("La valeur saisie est invalide (l'année est peut-être négative).")

annee = 0

while annee <= nombre:
    if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
        print(annee)
    annee += 1
os.system("PAUSE")
              
