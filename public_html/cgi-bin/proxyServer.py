import socket,threading

def analyzeRequest(message):
    print(message)
    messageArray = message.split("/")
    print ('did the first split')
    splittedMess = messageArray[1].split()
    print ('did the second split')
    print(splittedMess[0])
    return (splittedMess[0])
    
def check_whitelist(requestedPage):
    print('in check')
    acceptable = 1
    if requestedPage == "bing.com":
        print('its not facebook')
        acceptable = 0
        
    if requestedPage == "youtube.com":
        print('its not youtube')
        acceptable = 0
    
    
    print('out of ifs')
    return acceptable

def doTheThing(clientSocket, addr):
    #creating a proxy request socket
   
    try:
        while len(request) > 0 or len(response) > 0:
            # data received from client
            print("Request: ")
            requestedPage = analyzeRequest(request)
            clientIP, clientSocket = addr
            print(clientIP)
            print(clientSocket)
            acceptable = check_whitelist(requestedPage)
            print(acceptable)
            if acceptable == 1:
                print ('inside of this loop')
                clientSocket.send('''\
                HTTP/1.1 200 OK
                content-type: text/html
                content-length: 64

                <html>
                <body>
                    <h1>yeah it's not really working</h1>
                </body>
                </html>'''.encode())
                receive = mySocket.recv(2048)
                print(receive)
            break

    except Exception as e:
        print("6:" + str(e))
        # connection closed
        print("Connection closed")
        clientSocket.close()
        mySocket.close()



print_lock = threading.Lock()

portNumber = 12046


proxySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxySocket.bind(('', portNumber))
proxySocket.listen(5)

while True:
    # establish connection with client
    connectionSocket, addr = proxySocket.accept()
    connectionSocket.settimeout(5)
    print ("Connection from %s port %s" %addr)
    # Start a new thread and return its identifier
    
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #receiving the request from the client socket
    request = connectionSocket.recv(portNumber).decode()
    print(request)
    analyzed = analyzeRequest(request)
    print(analyzed)
    acceptable = check_whitelist(analyzed)
    if acceptable:
        print('yes its an acceptable website')
        mySocket.connect((analyzed, 80))
        rq = "GET / HTTP/1.1\r\nHost: %s" %analyzed
        mySocket.send(rq.encode())
        print (mySocket.recv(2048).decode())
        mySocket.close()
    else:
        print('not an acceptable website')
        errorMessage = ('''\
HTTP/1.1 200 OK
content-type: text/html
content-length: 64

<html>
<body>
<h1>ur in the wrong neighborhood champ</h1>
</body>
</html>''' )
        
        connectionSocket.send(errorMessage.encode())
        connectionSocket.close()
