import pygame
import time
from pygame.locals import *

def main():
	pygame.init()
	window = pygame.display.set_mode((720,480))

	Frames = pygame.time.Clock()

	run = True

	while run:
		Frames.tick(15)

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				run = False
				exit()

		pygame.display.flip()

if __name__ == "__main__":
	main()