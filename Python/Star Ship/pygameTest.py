import pygame
from random import randrange
from time import time
from os import system
from pygame.locals import *

debut = time()

pygame.init()

window = pygame.display.set_mode((720,480))
pygame.display.set_caption("Star Ship ma gueule! Music: Karsen Like to Known.")

pygame.mixer.music.load("kersen.wav")
pygame.mixer.music.play()
volume = 0.2
pygame.mixer.music.set_volume(volume)

background = pygame.image.load("espace_T.jpg").convert()
window.blit(background, (0,0))

perso = pygame.image.load("starship.png").convert_alpha()
positionPerso = perso.get_rect()
persoX = 0
persoY = 0
window.blit(perso, (persoX, persoY))


continuer = True
i = 0

pygame.key.set_repeat(50, 20)

mouse_move = False
timez = time()

while continuer:
	pygame.display.flip()
	pygame.mixer.music.set_volume(volume)
	if persoX < 680:
		if time() - timez > 0.05:
			
			persoX += 1
			timez = time()

	for event in pygame.event.get():
			if event.type == QUIT:
				continuer = False
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.mixer.music.pause()
				if event.key == K_RETURN:
					pygame.mixer.music.unpause()

				if event.key == K_RIGHT:
					perso = pygame.transform.rotate(perso, 45)
				if event.key == K_LEFT:
					perso = pygame.transform.rotate(perso, -45)

				if event.key == K_c:
					persoX = (720/2)-50
					persoY = (480/2)-50


				if event.key == K_DOWN:
					volume -= 0.1
				if event.key == K_UP:	
					volume += 0.1
					
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 4:
					volume += 0.10
				if event.button == 5:
					volume -= 0.10
			

			if event.type == MOUSEMOTION and event.buttons[0] == 1:
				if persoX  < event.pos[0] < persoX + 100:
					if persoY < event.pos[1] < persoY + 55:
							mouse_move = True
			if mouse_move:
				persoX = event.pos[0] -20
				persoY = event.pos[1] -20
			if event.type == MOUSEBUTTONUP:
				mouse_move = False
						

	window.blit(background, (0,0))
	window.blit(perso, (persoX, persoY))
