import pygame
from pygame.locals import *
import time
from random import randrange
from math import ceil, sqrt

SCALE = 740,480
MIDDLE = ceil(SCALE[0]/2), ceil(SCALE[1]/2)
def fixVals(values):
	newValues= list()
	for v in values:
		x = v[0] + MIDDLE[0]
		y = MIDDLE[1]-v[1]
		newValues.append((x,y))
	return newValues

def drawfonct(screen, fonct):
	x= -1000
	values = list()
	while x <= 1000:
		try:
			y = fonct(x)
		except:
			y =0

		values.append((x,y))
		x += 1
	values = fixVals(values)
	for i, v in enumerate(values):
		pygame.draw.line(screen, (0,0,0), (v[0], v[1]), (values[i-1][0], values[i-1][1]), 1)
def repere(screen):
	pygame.draw.line(screen, (0,0,0), (0, ceil(SCALE[1]/2)), (SCALE[0], ceil(SCALE[1]/2)), 2)
	pygame.draw.line(screen, (0,0,0), (ceil(SCALE[0]/2), 0),(ceil(SCALE[0]/2), ceil(SCALE[1])), 1)

def main():
	global SCALE

	pygame.init()
	screen = pygame.display.set_mode(SCALE)
	pygame.display.set_caption('Rain')
	timer = pygame.time.Clock()
	
	color1 = (200,200,200)
	f = lambda x: (x*x)

	while True:
		timer.tick(60)


		background = pygame.Surface(SCALE)
		#background = background.get_rect()
		#pygame.Surface.fill(color1, rect=background)
		screen.fill(color1)
		repere(screen)
		drawfonct(screen, f)

		for event in pygame.event.get():
			if event.type == QUIT:
				exit()


		pygame.display.flip()




if __name__ == "__main__":
	main()