import socket
import threading
from time import *
import os.path
from math import *

host = 'localhost'
port = 7777

class thread_recv(threading.Thread):
    def __init__(self, sock, dir):
        threading.Thread.__init__(self)
        self.sock = sock

        self.stt = False

        self.file = open(dir, 'ab')
    
    def run(self):
        self.stt = True
        while 1:
            data = b''
            try:
                data = self.sock.recv(4194304)
                if data != b'':
                    self.file.write(data)
                else:
                    break
            except socket.error:
                exit(0)

        self.stt = False

def fix_deb(deb):
    debit = floor(deb[0])
    unit = deb[1]

    units = ['o', 'k', 'm', 'g', 't']

    while len(str(floor(debit)))>3:
        debit = debit/1000
        it = units.index(unit)
        unit = units[it+1]

    debit = str(debit)
    
    add = False
    for n in str(deb):
        if add == True:
            debit += str(n)
        if n == '.':
            add == True

    return debit, unit





def main():
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_sock.connect((host, port))
    print('Connected to server')

    directory = input('Enter the directory where you would save the data: ')
    try:
        file = open(directory, 'wb')
    except:
        print('invalid directory.')
        exit(0)

    recv_file = thread_recv(serv_sock, directory)
    recv_file.start()
    tim = time()

    while 1:
        if recv_file.stt == False:
            break
    tim = time() - tim
    print('finish in '+str(tim))

    serv_sock.close()

    file.close()

    size = os.path.getsize(directory)
    debit = size/tim
    debit = fix_deb((debit, 'o') )
    print('size :'+str(size))
    print('debit: '+str(debit[0])+' '+str(debit[1])+'/s')

main()