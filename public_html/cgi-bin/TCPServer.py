#TCPServer.py
from _thread import *
import threading
from socket import socket, SOCK_STREAM, AF_INET

print_lock = threading.Lock()
def Main():

    #create a TCP socket
    #Notice the use of SOCK_DGRAM for UDP packets
    serverSocket = socket (AF_INET, SOCK_STREAM)
    serverPort=12048
    #Assign IP address and port number to socket
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    print ("Interrupt with CTRL-C")
    while True:
        try:
            connectionSocket, addr = serverSocket.accept()
            print_lock.acquire()
            print ("Connection from %s port %s" %addr)
        
            #start a thread
            start_new_thread(threaded, (connectionSocket, addr))
        
        except KeyboardInterrupt:
            print ("\nInterrupted by CTRL-C")
            break
    serverSocket.close()

def threaded(connectionSocket, addr):
    while True:
        #collect message and run process
        message = connectionSocket.recv(2048)
        if not message:
            print('Bye')
            # lock released on exit
            print_lock.release()
            break
        
        print ("Original message from client: ", message)
        print ("Address of client: ", addr)
        # Capitalize message from the client
        message = message.upper()
        connectionSocket.send(message)
        connectionSocket.close()


if __name__ == '__main__':
    Main()
