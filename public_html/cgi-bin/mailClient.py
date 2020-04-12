#!/usr/bin/python

import socket
import time
import cgi

def send_recv(socket, msg, code):
    if msg != None:
        print "Sending ==> ", msg
        socket.send(msg + '\r\n')

    recv = socket.recv(1024)
    print "<== Received: ", recv
    if recv[:3]!=code:
        print '%s reply not received from server.' % code
    return recv

def send(socket, msg):
    print "Sending ==> ", msg
    socket.send(msg + '\r\n')

print("Content-type: text/html\r\n\r\n")
print("<html><body>")
print("<h1>it works</h1>")
print("</body></html>")


# Message data goes to this server
serverName = 'smtp.cis.fiu.edu'
serverPort = 25

#Client Socket created
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Client connects to EmailServer
clientSocket.connect((serverName, serverPort))
#Check if FTP is ready to go on Mail Server
recv=send_recv(clientSocket, None, '220')


# E-mail content
clientName = "Sebastian"
userName="sgarc349"
userServer="fiu.edu"
toName="sgarc349"
toServer="fiu.edu"
subject="this is a test subject"
message = "This is my test message"



#Send HELO command and print server response.
heloCommand='EHLO %s' % clientName
recvFrom = send_recv(clientSocket, heloCommand, '250')
#Send MAIL FROM command and print server response.
fromCommand='MAIL FROM: <%s@%s>' % (userName, userServer)
recvFrom = send_recv(clientSocket, fromCommand, '250')
#Send RCPT TO command and print server response.
rcptCommand='RCPT TO: <%s@%s>' % (toName, toServer)
recvRcpt = send_recv(clientSocket, rcptCommand, '250')
#Send DATA command and print server response.
dataCommand='DATA'
dataRcpt = send_recv(clientSocket, dataCommand, '354')
#Send message data.



send(clientSocket, "Date: %s" % time.strftime("%a, %d %b %Y %H:%M:%S -0400", time.localtime()));
send(clientSocket, "From: %s@%s" % (userName, userServer));
send(clientSocket, "Subject: %s" %subject);
send(clientSocket, "To: %s@%s" % (toName, toServer));
send(clientSocket, ""); #End of headers
send(clientSocket, message);



#Message ends with a single period.
send_recv(clientSocket, ".", '250');
#Send QUIT command and get server response.
quitCommand='QUIT'
quitRcpt = send_recv(clientSocket, quitCommand, '221')
