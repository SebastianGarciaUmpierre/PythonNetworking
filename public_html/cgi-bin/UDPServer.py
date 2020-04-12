#UDPServer.py

from socket import socket, SOCK_DGRAM, AF_INET
import random

#This is UDP Socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',12049))
print ("Waiting for Connections")
while True:
    message, address = serverSocket.recvfrom(2048)
    print (message, address)
    rand = random.randint(0, 10)
    if rand < 3:
        print('Dropped the packet')
    else:
        message = message.upper()
        serverSocket.sendto(message, address)
serverSocket.close()
