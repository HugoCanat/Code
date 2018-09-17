import pygame
from pygame.locals import *
import os
from time import time
from random import randrange
def GameOver(window):
	texte = Score("Game Over")
	window.blit(texte, (90,200))
	pygame.display.flip()

	reset = True
	while reset:
		for event in pygame.event.get():
			if event.type == QUIT:
				reset = False
				pygame.quit()
				exit()



def Score(score):
	font = pygame.font.Font("FlapFont.ttf", 50)
	white = [255,255,255]
	score = str(score)
	text = font.render(score, True, white)

	return text

def main():
	clock = pygame.time.Clock()

	pygame.init()
	window = pygame.display.set_mode((430, 650))
	pygame.display.set_caption("Flappy Bird")

	background = pygame.image.load("background.jpg").convert()
	window.blit(background, (0,0))

	bande = pygame.image.load("bande.png").convert_alpha()
	bandeX, bandeY = 0, 0

	perso = pygame.image.load("Bird.png").convert_alpha()
	persoX, persoY = 75, 220
	window.blit(perso, (persoX, persoY))

	espace = 80
	########################################
	tuyauH = pygame.image.load("tuyauB.png")
	tuyauB = pygame.image.load("tuyauH.png")
	
	tuyauB_X = 450
	tuyauB_Y = randrange(170, 500)
	
	tuyauH_X = tuyauB_X
	tuyauH_Y = tuyauB_Y -476 - espace
	#########################################

	#########################################
	tuyau2H = pygame.image.load("tuyauB.png")
	tuyau2B = pygame.image.load("tuyauH.png")
	
	tuyau2B_X = 850
	tuyau2B_Y = randrange(170, 500)  
	
	tuyau2H_X = tuyau2B_X
	tuyau2H_Y = tuyau2B_Y -476 - espace
	#########################################
	play = True
	while play:
		pygame.display.flip()
		textePlay = Score("Press Space")
		Secondtxt = Score("to play")
		window.blit(textePlay, (60, 90))
		window.blit(Secondtxt, (110, 130))
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					play = False
	#########################################
	perso_move = 0

	score = 0
	time1 = time()
	timescore = True
	Scoretime = time()
	variable = 0
	jouer = True

	while jouer:

		clock.tick(150)

		pygame.display.flip()
		scoretxt = Score(score)

		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					perso_move = -1.43  
			if event.type == KEYUP:
				if event.key == K_SPACE:
					perso_move = 0.7
						
		persoY  += perso_move

		if time() - time1 > 0.005: #mouvement des objet
			bandeX -= 1
			tuyauB_X -= 1
			tuyauH_X -= 1

			tuyau2H_X -= 1
			tuyau2B_X -= 1
			time1 = time()

		if tuyauH_X < -102:              #remplacement des tuyau vers la droite si ils sont hors ecran
			tuyauH_X = tuyau2H_X + 300
			tuyauB_X = tuyauH_X
			tuyauB_Y = randrange(170, 500)
			tuyauH_Y = tuyauB_Y -476 - espace
		if tuyau2H_X < -102:
			tuyau2H_X = tuyauH_X + 300
			tuyau2B_X = tuyau2H_X
			tuyau2B_Y = randrange(170, 500)
			tuyau2H_Y = tuyau2B_Y -476 - espace


		if persoX+55 > tuyauH_X and persoX < tuyauH_X +100:
			if persoY+55 > tuyauB_Y or persoY < tuyauH_Y+450:
				GameOver(window)
				jouer = False

		if  persoX+55 > tuyau2H_X and persoX < tuyau2H_X+100:
			if persoY+55 > tuyau2B_Y or persoY < tuyau2H_Y+450:
				GameOver(window)
				jouer = False
			
		if time() - Scoretime > 2:
			if tuyauH_X == 75 or tuyau2H_X ==75:
				score += 1
				Scoretime = time()




		window.blit(background, (0,0))

		window.blit(tuyauH, (tuyauH_X, tuyauH_Y))
		window.blit(tuyauB, (tuyauB_X, tuyauB_Y))
		##################
		window.blit(tuyau2H, (tuyau2H_X, tuyau2H_Y))
		window.blit(tuyau2B, (tuyau2B_X, tuyau2B_Y))

		window.blit(bande, (0,0))
		window.blit(perso, (persoX, persoY))
		window.blit(scoretxt, (190, 100))



#fin du jeu
if __name__ == "__main__":
	main()


