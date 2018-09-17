import socket
import threading

host = 'localhost'
port = 7777

def main():
	directory = input('Enter the file directory: ')
	try:
		file = open(directory, 'rb')
	except:
		print("File doesn't exist.")
		exit(0)
	data = file.read()

	serv_sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serv_sock.bind((host, port))
	serv_sock.listen(5)

	client_sock, infos_client = serv_sock.accept()
	print(str(infos_client[0])+' is connected')

	client_sock.send(data)
	print('sending data...')


main()