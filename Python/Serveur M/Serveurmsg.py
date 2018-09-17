import threading
import socket

host = '192.168.1.18'
port = 7777


class ThreadClient(threading.Thread):
	def __init__(self, sock):
		threading.Thread.__init__(self)
		self.sock = sock

	def run(self):
		nom = self.getName()
		while 1:
			try:
				msg = self.sock.recv(4096)
				if msg.decode().upper() == 'FIN':
					break

				print('message: '+msg.decode()+' users '+nom)
				for client in clients_sock:
					if client != nom:
						clients_sock[client].send(msg)
			except ConnectionResetError:
				print(nom + ' deconected')
				break

		self.sock.close()
		del clients_sock[nom]
		print('Client '+nom +' déconnecté')

clients_sock = {}
def main():
	main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	main_socket.bind((host, port))
	main_socket.listen(5)
	print('listening on port '+str(port))

	server_on = True
	
	print('Server on. Waiting for clients..')
	while server_on:
		sock, info = main_socket.accept()
		print(str(info)+ ' is connected.')
		th = ThreadClient(sock)
		th.start()
		n = th.getName()
		clients_sock[n] = sock
		sock.send(b'You are connected you can send messages')
		
		




main()