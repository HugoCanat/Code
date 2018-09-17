import socket
import threading
import signal

hote = "192.168.1.23"
port = 7777

port = input('Enter the port: ')
if port == '' or port == '\n':
	port = 7777

def stop():
	th1.__Thread__stop()
	th2.__Thread__stop()
	exit(0)

class ThreadSend(threading.Thread):
	def __init__(self, sock):
		threading.Thread.__init__(self)
		self.sock = sock

	def run(self):
		while 1:
			msg = input('>')
			msg = msg.encode()
			self.sock.send(msg)

class ThreadRecv(threading.Thread):
	def __init__(self, sock):
		threading.Thread.__init__(self)
		self.sock = sock

	def run(self):
		while 1:
			msg = self.sock.recv(4096)
			msg = msg.decode()
			if msg == None:
				break

			print('\n'+msg+'\n>')

		self.__Thread__stop()

th1 = None
th2 = None
def main():
	server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_sock.connect((hote, int(port)))
	print("Connexion etablished with {}".format(port))

	global th1, th2

	th1 = ThreadRecv(server_sock)
	th2 = ThreadSend(server_sock)
	th1.start()
	th2.start()


signal.signal(signal.SIGINT, stop)
main()
