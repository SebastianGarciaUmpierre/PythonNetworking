from socket import socket,AF_INET, SOCK_STREAM

serverName = 'localhost'
serverPort = 12048
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print ('here we are')
message = 'GET /test.cgi HTTP/1.1'
clientSocket.send(message)
thing = clientSocket.recv(2048)
print (thing)
clientSocket.clos()
