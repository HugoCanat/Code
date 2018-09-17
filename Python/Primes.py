from math import *
import time
from os import system
import threading

class calcThread(threading.Thread):
	def __init__(self, start_nb, nb, nb_th):
		threading.Thread.__init__(self)
		self.nb = nb
		self.start_nb = start_nb
		self.nb_th = nb_th

		self.st = False
		self.primes_number = []

	def run(self):
		self.st = True
		a = 0
		i = self.start_nb

		while a < self.nb+1:
			if premier(i):
				a += 1
				self.primes_number.append(i)
			i+= self.nb_th*2
		self.st= False


def wrtNb(*l):
	f =  open('PrimeIterations.p', 'w')
	for li in l:
		for nb in li:
			f.write(str(nb)+'\n')

	f.close()


def premier(nb):
	i = 2
	b = ceil(sqrt(nb))+1
	y = 1

	if nb % 2 != 0:
		y = 2
		i = 3

	while i < b:
		if nb % i == 0:
			return False		
		i += y

	return True

def Main():
	nombre = int(input('Number: '))
	time_start = time.time()

	th1 = calcThread(3,nombre/4,4)
	th2 = calcThread(5,nombre/4,4)
	th3 = calcThread(7,nombre/4,4)
	th4 = calcThread(9,nombre/4,4)

	th1.start()
	th2.start()
	th3.start()
	th4.start()

	while 1:
		if th1.st == False and th2.st == False and th3.st == False and th4.st == False:
			break

	time_end = time.time() - time_start
	wrtNb(th1.primes_number, th2.primes_number, th3.primes_number, th4.primes_number)
	print(time_end)
	system('PrimeIterations.p')


if __name__ == '__main__':
	Main()