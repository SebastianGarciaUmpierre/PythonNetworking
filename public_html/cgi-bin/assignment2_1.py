from socket import AF_INET, SOCK_STREAM, socket

def main():
    serverSocket = openTcpSocket(12049)
    
    while True:
        try:
            print ('1. Ready to serve...')
            connectionSocket, addr = serverSocket.accept()
            print ('2. Connection received from', addr)
            message = connectionSocket.recv(4096).decode()
            filename = message.split()[1].partition("/")[2]
            print('3. Client is requesting file: %s' %filename)

            # Send file if it exists
            sendFile(connectionSocket, filename, "text/plain")
            connectionSocket.close()
        except IOError:
            print('4. %s does not exist' % filename)
            sendError(connectionSocket,'404','Not Found')
        except KeyboardInterrupt:
            print("\nInterrupted by CTRL-C")
            break
    serverSocket.close()

def sendError(connectionSocket, id, desc):
    print ('5. Inside sendError')
    errorMessage = ('''\
HTTP/1.1 200 OK
content-type: text/html
content-length: 64

<html>
<body>
    <h1>Error %s: Under Construction</h1>
</body>
</html>''' %id)

    connectionSocket.send(errorMessage.encode())
    connectionSocket.close()
    
def sendFile(connectionSocket, filename, data):
    print('5. Inside of sendFile')
    f = open(filename, 'r')
    fullMsg =''
    for line in f:
        fullMsg += line
        fullMsg += "<br>"
    fullMsg += "</body></html>"
    contentLength = len(fullMsg)
    httpResponse ='''\
HTTP/1.1 200 OK
content-type: text/html
content-length: {0}

<html>
<body>
'''.format(contentLength)
    
    connectionSocket.send(httpResponse.encode())
    connectionSocket.send(fullMsg.encode())
    f.close()
    print ('6. Done sending file')

def openTcpSocket(serverPort):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    return serverSocket

if __name__== "__main__":
    main()
