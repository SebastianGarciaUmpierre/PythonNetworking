#!/usr/bin/python

import cgi
import sys

sys.stderr = sys.stdout

  
  
print("Content-type: text/html\r\n\r\n")
print("<html><body>")

# Using the inbuilt methods
form = cgi.FieldStorage()
if form.getvalue("emailTo"):
    emailTo = form.getvalue("emailTo")
    emailTo = emailTo.split('@')
    print("<h1>"+ emailTo[0] + "</h1>")
    print("<h2>" + emailTo[1] + "</h2>")
if form.getvalue("emailFrom"):
    emailFrom = form.getvalue("emailFrom")
    emailFrom = emailFrom.split('@')
    print("<h1>"+ emailFrom[0] + "</h1>")
if form.getvalue("Subject"):
    subject = form.getvalue("Subject")
    print("<h2>" + subject + "</h2>")
if form.getvalue("Message"):
    message = form.getvalue("Message")
    print("<h2>"+ message+ "</h2>")
  
print ("</body></html>")
