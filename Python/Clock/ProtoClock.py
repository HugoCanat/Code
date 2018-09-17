import pygame
from pygame.locals import *
from math import ceil, sqrt, floor, radians, cos
import os
import time

SCALE = 200
SCALE2 = SCALE + ceil(SCALE/9)
DECA = SCALE/10
CENTERX = round(SCALE/2)
CENTERY = round((SCALE/2))#-(DECA/2))
RADIUS = ceil(SCALE/2.1)#-((DECA/2)+10)

def ClockUpdate(screen, hours, mins, secs, font):
	white = (255,255,255)
	back = (35,40,48)
	white = (100,100,100)
	orange = (255, 127, 39)
	black=(0,0,0)
	red = (255,0,0)
	green = (0,255,64)
	blue = (66,168,223)

	screen.fill((back))
	HoursSeq(screen, blue, 60, ceil(RADIUS/15), ceil((RADIUS/15)/5))
	HoursSeq(screen, red, 12, ceil(RADIUS/9), ceil((RADIUS/9)/4))
	
	minute_needle(screen, mins, blue)
	second_needle(screen, secs, (45,126,166))
	hour_needle(screen, hours, red)

	pygame.draw.circle(screen, back, (CENTERX,CENTERY), 6)
	pygame.draw.circle(screen, blue, (CENTERX,CENTERY), 3)
	affi_time2(screen, font, hours, mins, secs)

def affi_time2(screen, font, hours=0, mins=0, secs=0):
	hours = floor(hours)
	mins = floor(mins)
	if hours < 10.0:
		hours = "0" + str(hours)
	if mins < 10.0:
		mins = "0" + str(mins)
	if secs < 10.0:
		secs = "0" + str(secs)
	hours = str(hours) 
	mins = str(mins)
	secs = str(secs)

	time = font.render(hours +" : " +mins+" : " + secs, 1, (255,255,255))
	pygame.draw.line(screen, (0,0,0), (0,SCALE), (0, SCALE2), 3 )
	screen.blit(time, (5,SCALE))

def get_time(timep):
	secs = round(timep%60, 3)
	mins = round(((timep/60)%60), 1)
	hours = round(timep/3600, 1)
	return hours, mins, secs

def hour_needle(screen, hours, color):

	angle = get_angle(hours%12, 12)
	hauteur, cos_pos = get_coor(radians(angle), RADIUS-(DECA/1.2))
	hauteur = round(hauteur, 1)

	if angle >= 360:
		angle = 0
	if angle < 0:
		angle = 360

	if angle <= 180:
		pygame.draw.line(screen, color, (CENTERX,CENTERY), (CENTERX+cos_pos, CENTERY-round(hauteur)), ceil(RADIUS/80))
	else:
		pygame.draw.line(screen, color, (CENTERX,CENTERY), (CENTERX-cos_pos, CENTERY-round(hauteur)), ceil(RADIUS/80))

def minute_needle(screen, mins, color):

	angle = get_angle(mins)
	hauteur, cos_pos = get_coor(radians(angle), RADIUS-(RADIUS/15)-(DECA/3) )
	hauteur = round(hauteur, 1)

	if angle >= 360:
		angle = 0
	if angle < 0:
		angle = 360

	if angle <= 180:
		pygame.draw.line(screen, color, (CENTERX,CENTERY), (CENTERX+cos_pos, CENTERY-round(hauteur)), ceil(RADIUS/50))
	else:
		pygame.draw.line(screen, color, (CENTERX,CENTERY), (CENTERX-cos_pos, CENTERY-round(hauteur)), ceil(RADIUS/50))

def second_needle(screen, secs, color):
	angle = get_angle(secs)
	hauteur, cos_pos = get_coor(radians(angle))
	hauteur = round(hauteur, 1)

	if angle >= 360:
		angle = 0
	if angle < 0:
		angle = 360

	if angle <= 180:
		pygame.draw.line(screen, color, (CENTERX,CENTERY), (CENTERX+cos_pos, CENTERY-round(hauteur)), ceil(RADIUS/90))
	else:
		pygame.draw.line(screen, color, (CENTERX,CENTERY), (CENTERX-cos_pos, CENTERY-round(hauteur)), ceil(RADIUS/90))

def HoursSeq(surface, color, unit, high, width, instant = False):
	degre = round((360/unit), 4) #360/12H = 30

	angle = 0
	
	while angle != 360:
		sin, cos = get_coor(radians(angle), RADIUS-2)
		sin2, cos2 = get_coor(radians(angle), RADIUS-high)
		if angle <= 180:
			pygame.draw.line(surface, color, (CENTERX+cos2,CENTERY-sin2), (CENTERX+cos,CENTERY-sin), width)
		else:
			pygame.draw.line(surface, color, (CENTERX-cos2,CENTERY+sin2), (CENTERX-cos,CENTERY+sin), width)

		angle += degre

def get_coor(angle, high = RADIUS):
	hauteur = cos(angle)*high
	width = sqrt((high*high) - (hauteur*hauteur))
	return hauteur, width

def get_angle(timep, div=60):
	coef = 360
	time_spend = timep
	#360 degree, for 60 seconde
	if time_spend != 0:
		coef = div/time_spend
	if coef == 360:
		return 0
	else:
		return 360/coef

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCALE,SCALE2))
	pygame.display.set_caption("Clock")

	hauteur = RADIUS
	angle = 0
	center= ceil(SCALE/2)
	time_s0,pend = time.time()
	
	white = (255,255,255)
	back = (35,40,48)
	white = (100,100,100)
	orange = (255, 127, 39)
	black=(0,0,0)
	red = (255,0,0)
	green = (0,255,64)
	blue = (66,168,223)

	font = pygame.font.SysFont(None, ceil(DECA*1.92))
	clock = pygame.time.Clock()

	timeT = 0
	run = True
	while True:
		clock.tick(120)

		if run:
			timep = time.time() - time_spend

		hours, mins, secs = get_time(timep)

		if run:

			for event in pygame.event.get():
				if event.type == QUIT :
					pygame.quit()
					exit()
				if event.type == MOUSEBUTTONDOWN:
					run = False
					timeT = timep + time_spend


			ClockUpdate(screen, hours, mins, secs, font)
			
			pygame.display.flip()

		else :
			for event in pygame.event.get():
				ClockUpdate(screen, hours, mins, secs, font)

				if event.type == MOUSEBUTTONDOWN:
					time_spend = time.time() - timep
					run = True
				if event.type == QUIT:
					pygame.quit()
					exit()
			

if __name__ == '__main__':
	main()