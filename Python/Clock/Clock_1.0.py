import pygame
from pygame.locals import *
from math import ceil, sqrt, floor, radians, cos
import os
import time

SCALE = 350
RADIUS = ceil(SCALE/2)-5
CENTERX = ceil(SCALE/2)
CENTERY = CENTERX

class Clock:
	def __init__(self, Screen, scale, centerx, centery):
		self.scale = scale
		self.screen = Screen
		self.centerx = centerx
		self.centery = centery
		
		self.time_spend = False
		self.pause_spend = False
		self.pausep = False
		self.timep = False
		
		self.hours = 0.0
		self.mins = 0.0
		self.secs = 0.0

		self.second_color = (255,255,0)
		self.minute_color = (0,0,255)
		self.hour_color = (255,0,0)
		self.hoursDiv_color = (255,50,50)
		self.minutesDiv_color = (0,255,12)
		self.BackColor = (0,0,0)

		self.font = pygame.font.SysFont(None, ceil(SCALE/10))
		self.TimePrecision = 3
		self.text_centerx, h = self.font.size('00 : 00 : 00.'+'0'*self.TimePrecision)

	def Pause(self):
		if self.pause_spend == False:
			self.pause_spend = time.time()

		self.pausep = time.time() - self.pause_spend

	def Run(self):
		if self.time_spend == False:
			self.time_spend = time.time()

		if self.pause_spend:
			self.time_spend += self.pausep
			self.pause_spend = False
			self.pausep = False

		self.timep = (time.time() - self.time_spend) * 100
		self.GetTime()
		#self.hours *= 25000
		#self.mins *= 300
		#self.secs *= 1



		self.screen.fill((0,0,0))
		#pygame.draw.circle(self.screen, self.minutesDiv_color, (CENTERX,CENTERY), self.scale+5, 2)
		#self.SecondeCircle()

		self.ClockDiv(self.minutesDiv_color, 60, 5, 2, 60)
		self.ClockDiv(self.hoursDiv_color, 12, 8, 4, 12)
		
		
		self.second_needle()
		self.minute_needle()
		self.hour_needle()

		
		self.Time()
		self.text_centerx, h = self.font.size('00 : 00 : 00.'+'0'*self.TimePrecision)

		pygame.draw.circle(self.screen, self.BackColor, (CENTERX,CENTERY), 5)
		pygame.draw.circle(self.screen, self.minute_color, (CENTERX,CENTERY), 2)

		pygame.display.flip()

	def hour_needle(self):
		angle = self.GetAngle(self.hours, div=12)
		high, cos = self.GetCoor(radians(angle), self.scale-20)
		
		if angle <= 180:
			pygame.draw.line(self.screen, self.hour_color, (self.centerx, self.centery),\
			 (self.centerx+cos, self.centery-round(high)), 3)
		else:
			pygame.draw.line(self.screen, self.hour_color, (self.centerx, self.centery),\
			 (self.centerx-cos, self.centery-round(high)), 3)

	def minute_needle(self):
		angle = self.GetAngle(self.mins)
		high, cos = self.GetCoor(radians(angle), self.scale-13)
		
		if angle <= 180:
			pygame.draw.line(self.screen, self.minute_color, (self.centerx, self.centery),\
			 (self.centerx+cos, self.centery-round(high)), 3)
		else:
			pygame.draw.line(self.screen, self.minute_color, (self.centerx, self.centery),\
			 (self.centerx-cos, self.centery-round(high)), 3)

	def second_needle(self):
		angle = self.GetAngle(self.secs)
		high, cos = self.GetCoor(radians(angle), self.scale)
		
		if angle <= 180:
			pygame.draw.line(self.screen, self.second_color, (self.centerx, self.centery),\
			 (self.centerx+cos, self.centery-round(high)), 2)
		else:
			pygame.draw.line(self.screen, self.second_color, (self.centerx, self.centery),\
			 (self.centerx-cos, self.centery-round(high)), 2)	
	
	def ClockDiv(self, color=(0,255,0), unit=60, high=15, width=5, number=60):
		degre = round((360/unit), 4)
		angle = 0
		Nb = 1

		while Nb <= number:
			sin, cos = self.GetCoor(radians(angle), self.scale)
			sin2, cos2 =  self.GetCoor(radians(angle), self.scale-high)

			if angle <= 180:
				pygame.draw.line(self.screen, color, (self.centerx+cos2,self.centery-sin2),\
				 (self.centerx+cos,self.centery-sin), width)
			else:
				pygame.draw.line(self.screen, color, (self.centerx-cos2,self.centery-sin2),\
				 (self.centerx-cos,self.centery-sin), width)
			angle += degre
			Nb += 1

	def GetCoor(self, angle, high):
		hauteur = cos(angle)*high
		width = sqrt((high*high) - (hauteur*hauteur))
		return hauteur, width

	def GetTime(self):
		self.secs = self.timep%60
		self.mins = (self.timep/60)%60
		self.hours = self.timep/3600

	def GetAngle(self, timep, div=60):
		coef = 360
		if timep != 0:
			coef = div/timep 

		return (360/coef)%360

	def Time(self):
		if self.TimePrecision > 10:
			self.TimePrecision = 10

		hours = floor(self.hours)
		mins = floor(self.mins)
		secs = self.secs
		if hours < 10.0:
			hours = "0" + str(hours)
		if mins < 10.0:
			mins = "0" + str(mins)
		if secs < 10.0:
			secs = "0" + str(secs)
		hours = str(hours) 
		mins = str(mins)

		secs = str(secs)
		secs = list(secs)
		
		i = 1
		secondes = secs[0]
		try :
			while i <= self.TimePrecision + 2:
				secondes += secs[i]
				i += 1
		except IndexError:
			pass

		text = str(hours +" : " +mins+" : " + secondes)
		time = self.font.render(text, 1, (255,255,255))

		self.screen.blit(time, (self.centerx-(ceil(self.text_centerx/2)),230))

	def SecondeCircle(self):
		if floor(self.mins) % 2:
			actAngle = self.GetAngle(self.secs)
			angle = 360
			color = (255,0,0)

			while actAngle <= angle:
				sin, cos = self.GetCoor(radians(actAngle), self.scale+6)
				sin2, cos2 = self.GetCoor(radians(actAngle), self.scale+5)
				if actAngle <= 180:
					pygame.draw.line(self.screen, color, (self.centerx+cos2,self.centery-sin2),\
					 (self.centerx+cos,self.centery-sin), 3)
				else:
					pygame.draw.line(self.screen, color, (self.centerx-cos2,self.centery-sin2),\
					 (self.centerx-cos,self.centery-sin), 3)
				actAngle += 0.5

		else:
			angle = self.GetAngle(self.secs)
			actAngle = 0.0
			color = (255,0,0)
			while actAngle <= angle:
				sin, cos = self.GetCoor(radians(actAngle), self.scale+6)
				sin2, cos2 = self.GetCoor(radians(actAngle), self.scale+5)
				if actAngle <= 180:
					pygame.draw.line(self.screen, color, (self.centerx+cos2,self.centery-sin2),\
					 (self.centerx+cos,self.centery-sin), 3)
				else:
					pygame.draw.line(self.screen, color, (self.centerx-cos2,self.centery-sin2),\
					 (self.centerx-cos,self.centery-sin), 3)
				actAngle += 0.5

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCALE,SCALE))
	pygame.display.set_caption("Clock")

	timer = pygame.time.Clock()

	NumClock = Clock(screen, RADIUS-5, 175, 175)
	NumClock.second_color = (238,64,34)
	NumClock.minute_color = (51,144,240)
	NumClock.hour_color = (164,204,45)
	NumClock.hoursDiv_color = (172,47,47)
	NumClock.minutesDiv_color = (81,132,183)

	Run = False
	NumClock.Run()
	NumClock.Pause()
	while True:
		timer.tick(120)
		if Run:
			NumClock.Run()
		else:
			NumClock.Pause()

		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
			if event.type == MOUSEBUTTONDOWN:
				if Run :
					Run = False
				else :
					Run = True
			if event.type == KEYDOWN:
				Run = False
				NumClock.time_spend = 0.0
				NumClock.timep = 0.0
				NumClock.hours = 0.0
				NumClock.mins = 0.0
				NumClock.secs = 0.0
				pygame.display.flip()

		pygame.display.flip()


if __name__ == "__main__":
	main()