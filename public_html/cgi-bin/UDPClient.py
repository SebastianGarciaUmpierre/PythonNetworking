#UDPClient.py
import time
from socket import socket, SOCK_DGRAM, AF_INET


serverName = 'ocelot.aul.fiu.edu'
serverPort = 12049
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
message = raw_input('Input lowercase sentence: ')
startTime = time.time()
clientSocket.sendto(message, (serverName, serverPort))
modifiedMessage, addr = clientSocket.recvfrom(2048)
endTime = time.time()
duration = round((endTime - startTime),5)
print 'IP:', addr[0]
print 'Port: ', addr[1]
print  'Modified message: ', modifiedMessage
print 'RTT: ', duration, 'seconds'
clientSocket.close()
