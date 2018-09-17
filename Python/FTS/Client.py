import threading 
import socket
import math 


def pannel_command(command):
	#defini les commandes utilisateurs
	command_list = ["stop", "envoyer", "accepter", "recevoir", "liste_clients", "annuler"]

def main():
	print("<<   File Tansfert System Client   >>")

	#on creer le socket du serveur 
	main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#on demande l'adresse et le port de la machine ou du réseau hébergeant le système
	#On vérifie l'intégrité du port 
	p = 1
	while p:
		port = input("Entrez le port de la machine hote: ")
		try:
			port = int(port)
			p = 0
		except ValueError:
			print('/!\ Port invalide.')
			p = 1
	#de même pour l'adresse ip
	p=1
	while p:
		host = input("Entrez l'adresse de la machine hote: ")
		try:
			main_socket.connect(("192.168.1.18",port))
			p = 0
		except:
			print("/!\ Adresse IP invalide.")
			p = 1

	print('Connexion établie')
	id_client = main_socket.recv(1024).decode()

	stop = 0
	while stop != 1:
		command = input('> ')





if __name__ == '__main__':
	main()