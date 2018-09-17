import socket
import threading



def main():
	print("<<   File Tansfert System Client  >>")
	
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	client.connect(('localhost', 7777))

	msg = client.recv(1024)
	print(msg.decode())

if __name__ == '__main__':
	main()