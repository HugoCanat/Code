import threading 
import socket
import math 

dict_client = {}

#le but de ce thread est de gerer les clients et de leur permettre de communiquer
class Thread_Client(threading.Thread):
	def __init__(self, socket_client, id_client):
		threading.Thread.__init__(self)
		self.socket_client = socket_client
		self.id_client = id_client

	def run(self):
		self.socket_client.send(str(self.id_client).encode())
		

		



def main():
	print("<<   File Tansfert System   >>")

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
			main_socket.bind(("192.168.1.18",port))
			p = 0
		except:
			print("/!\ Adresse IP invalide.")
			p = 1

	main_socket.listen(10)

	print("\nLe serveur est en exécution.")
	print("  Adresse IP: {}".format(host))
	print("  Port utilisé: {}".format(port))

	nb_client = 0
	while True:
		client, info = main_socket.accept()
		thread_client = Thread_Client(client, nb_client)
		thread_client.run()
		
		dict_client[nb_client] = (client, info)
		nb_client += 1



if __name__ == '__main__':
	main()