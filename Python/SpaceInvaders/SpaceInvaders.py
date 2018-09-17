import pygame
from pygame.locals import *
import time

SCREENWIDTH = 800
SCREENHIGHT = 600

def main():
	pygame.init()

	clock = pygame.time.Clock()

	BLACK = (0,0,0)

	screen = pygame.display.set_mode((SCREENWIDTH, SCREENHIGHT))

	ship = pygame.image.load("assets/Ship.png").convert_alpha()
	shipX = SCREENWIDTH/2 - 58/2
	shipY = SCREENHIGHT - 32*2

	bullet = pygame.image.load("assets/Bullet.png").convert()
	bulletX = 800
	bulletY = 600

	pygame.mouse.set_pos(shipX, shipY)
	pygame.mouse.set_visible(0)

	pygame.key.set_repeat(1, 1)

	fire = False

	while True:
		clock.tick(100)
		shipX, y = pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				exit()
			if event.type == KEYDOWN:
				if event.key == K_RIGHT:
					shipX += 10
					pygame.mouse.set_pos(shipX, y)
				if event.key == K_LEFT:
					shipX -= 10
					pygame.mouse.set_pos(shipX, y)
				if event.key == K_SPACE and fire == False:
					bulletX = shipX
					bulletY = shipY
					fire = True
			if event.type == MOUSEBUTTONDOWN and fire == False:
				bulletX = shipX
				bulletY = shipY
				fire = True

		if shipX <= 0:
			pygame.mouse.set_pos(0, y)

		if fire:
			bulletY -= 10
		if bulletY < -10:
			fire = False

		screen.fill(BLACK)
		screen.blit(bullet, (bulletX, bulletY))
		screen.blit(ship, (shipX-58/2,shipY))
		pygame.display.update()





if __name__ == "__main__":
	main()