from tkinter import *
from math import *
import time
from random import randrange
SCALE = (630, 630)

class Interface(Frame):

	def __init__(self, screen):
		Frame.__init__(self, screen)
		self.pack(fill=BOTH)

		self.cols= 3
		self.lines = list()
		self.doors = list()
		self.cases_dict = dict()

		self.can = Canvas(self, bg='light grey', height=SCALE[0], width=SCALE[0])
		self.can.pack(side=LEFT)

		self.but = Button(self, text='Generate\nMaze', command=self.draw_maze).pack()

		self.sv = StringVar()
		self.lab = Label(self, text='Lines').pack()

		self.spin = Spinbox(self, from_=2, to=150, increment=1, textvariable=self.sv, command=self.draw_tab).pack()

	def draw_tab(self):
		self.cols = int(self.sv.get())

		self.can.delete(ALL)
		self.lines = list()

		Hcol = (SCALE[0]-2)/self.cols
		
		x1,y1 = 2,2
		x2, y2 = x1, SCALE[0] 
		self.can.create_line(x1,y1,x2,y2, width=2)
		

		x1, y1 = x1+Hcol, y1
		x2, y2 = x1, SCALE[0]

		l = 1
		while l < self.cols:
			self.can.create_line(x1,y1,x2,y2, width=2)
			self.lines.append([x1,y1,x2,y2])
			
			x1, y1 = x1+Hcol, y1
			x2, y2 = x1, SCALE[0]
			l += 1
			

		x1,y1 = 2,2
		x2, y2 = SCALE[0], y1
		self.can.create_line(x1,y1 ,x2,y2, width=2)
		x1, y1 = x1, y1+Hcol
		x2, y2 = SCALE[0], y1

		l = 1
		while l < self.cols:
			self.can.create_line(x1,y1 ,x2,y2, width=2)
			self.lines.append([x1,y1,x2,y2])
			
			x1, y1 = x1, y1+Hcol
			x2, y2 = SCALE[0], y1
			
			l += 1

		self.can.create_line(2, SCALE[0], SCALE[0], SCALE[0], width=2)
		self.can.create_line(SCALE[0],2, SCALE[0], SCALE[0], width=2)

	def Sdoors(self):
		self.doors = list()
		
		for i, c in enumerate(self.lines):
			door = list()
			if i < len(self.lines)/2:
				
				p = (c[3] - c[1])/self.cols
				door = c
				door[3] = door[1]+p-2
				i = 1
				while i <= self.cols:
					self.doors.append(list(door))
					door[1] += p
					door[3] += p

					i+= 1

			else:
				
				p = (c[2] - c[0])/self.cols
				door = c
				door[2] = door[0]+p-2
				i = 0
				while i < self.cols:
					self.doors.append(list(door))
					door[0] += p
					door[2] += p

					i += 1

		#print(self.doors, len(self.doors))

		""" fonction for pour remettre les coordonnées des lignes droit"""
		for i, door in enumerate(self.doors):
			if i < len(self.doors)/2:
				door[1] += 1
				door[3] += 1
			else:
				door[0] += 1
				door[2] += 1

	def define_cases(self):
		lenght = len(self.doors)
		self.cases_dict = dict()

		for nb, doors in enumerate(self.doors):
			if nb < lenght/2:
				self.cases_dict[nb] = (nb*self.cols-(((self.cols*self.cols)-1)*floor(nb/self.cols)), nb*self.cols-(((self.cols*self.cols)-1)*floor(nb/self.cols))+1)
			else:
				self.cases_dict[nb] = (nb-lenght/2, nb-lenght/2+self.cols)
		
		#print(self.cases_dict)


	def draw_maze(self):
		self.draw_tab()
		self.Sdoors()
		self.define_cases()


		openDoor = list()

		#creation list des valeurs des cases associé a leur numero
		valCases = list()
		i = 0
		while i < (self.cols*self.cols):
			valCases.append(i)
			i+=1 

		while len(openDoor) < (self.cols**2)-1:
			#choix de la porte
			randDoor = randrange(0, len(self.cases_dict))
			while randDoor in openDoor:
				randDoor = randrange(0, len(self.cases_dict))
			

			
			#numero des cases
			case1 = int(self.cases_dict[randDoor][0])
			case2 = int(self.cases_dict[randDoor][1])
			#verif numero associés
			if valCases[case1] != valCases[case2]:#si les numero des deux cases sont différents
				openDoor.append(int(randDoor))

				v = valCases[case2]
				#on met toutes les cases qui on le meme numero que la case2 a la valeur de case1
				for i, Val in enumerate(valCases):
					if Val == v:
						valCases[i] = valCases[case1]

		#Affichage de l'ouverture des portes
		#print('openDoor' +str(openDoor))
		#print('value Cases'+str(valCases))

		self.can.create_rectangle(3,3, self.doors[0][0]-1, self.doors[0][0]-1, fill='green')
		self.can.create_rectangle(SCALE[0]-1,SCALE[1]-1, SCALE[0]-self.doors[0][0]+3, SCALE[0]-self.doors[0][0]+3, fill='red')
		for d in openDoor:
			door = self.doors[d]
			self.can.create_line(door[0], door[1], door[2], door[3], fill='light grey', width=3)
		


def main():

	screen = Tk()
	screen.title('Random Maze')

	interface = Interface(screen)

	
	interface.mainloop()


if __name__ == '__main__':
	main()