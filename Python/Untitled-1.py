import socket
import threading

host = 'localhost'
port = 7777

def main():
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_sock.connect((host, port))
    print('Connected to server')
    data = serv_sock.recv(1048576)
    print('data receved.')

    directory = input('Enter the directory where you would save the data: ')
    try:
        file = open(directory, 'wb')
    except:
        print('invalid directory.')
        exit(0)

    file.write(data)

main()