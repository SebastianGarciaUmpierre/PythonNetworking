from socket import socket, SOCK_STREAM, AF_INET


def readHeaders(connectionSocket):
    message = connectionSocket.recv(2048).decode()
    if not message:
        print('bye')
    print ("Original Message from Client: ", message)
    langOne = message.split("Accept-Language:")
    langTwo = langOne[1]
    langThree = langTwo.split(";")
    language = langThree[0].strip()
    print (language)
    return language

def acceptLanguageModifyFile(filename, language):
    filename = "hello.html"
    
    language = language.split(",")
    languageOne = language[0]
    print (languageOne)
    languageTwo = language[1]
    print (languageTwo)
    
    print(languageOne > 'es' )
    print (languageOne < 'es')
    print (languageOne == 'es')
    
    if (languageOne == 'en') or (languageTwo == 'en'):
        filename = filename + ".en"
    if (languageOne == 'es'):
        filename = filename + ".es"
    if (languageOne == 'de'):
        filename = filename + ".de"
    return filename

def sendFile(connectionSocket, filename, words, data):
    print('5. Inside of sendFile')
    f = open(filename, 'r')
    print ("Reading from: ", filename)
    fullMsg =''
    contentLength = 50
    for line in f:
        fullMsg += line
        fullMsg += "<br>"
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


def Main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', 12049))
    serverSocket.listen(1)
    buf = ""
    key = None
    modified = None
    
    while True:
        try:
            print ('Ready to serve...')
            connectionSocket, addr = serverSocket.accept()
            language = readHeaders(connectionSocket)
            print (language)
           # filename = headers ["STATUS-LINE"].split()[1].partition("/")[2]
           # print ("Status Line: ", headers["STATUS-LINE"])
            filename = "hello.html"
            filenameLanguage = acceptLanguageModifyFile(filename, language)
            print("\n\n\n\n")
            print(filenameLanguage)
            seconds = None
           # if filenameLanguage == filename:
           #     seconds = ifModifiedSinceSeconds(headers)
            sendFile(connectionSocket, filenameLanguage, "text/plain", seconds)
          # connectionSocket.shutdown(SHUT_WR)
            connectionSocket.close()
        except IOError:
            print ("Not Found %s" %filename)
            sendError(connectionSocket, '404', 'Not Found')
            connectionSocket.shutdown(SHUT_WR)
            connectionSocket.close()
        except KeyboardInterrupt:
            print ("\nInterrupted by CTRL-C")
            break
    serverSocket.close()


if __name__ == '__main__':
    Main()
