#!/usr/bin/env python

import cgi, smtplib

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
ontvanger = form.getvalue('ontvanger')
subject = form.getvalue('subject')
tekstveld = form.getvalue('tekstveld')

print ("Content-type:text/html\n\n")
print "<html>"
print "<head>Hello Wie?</head> <body>"
print '<form action="index.py" method="post">'
print 'Ontvanger: <input type="text" name="ontvanger" /><br/>'
print 'Subject: <input type="text" name="subject"><br />'
print 'Tekstveld: <input type="text" name="tekstveld"><br />'
print '<input type="submit" value="Submit" />'
print ("<h2>Hello %s %s %s</h2>" % (ontvanger, subject, tekstveld))

port = 1025
smtp_server = "localhost"
sender_email = "admin@localhost.com"
receiver_email = ontvanger
message = 'Subject: {}\n\n{}'.format(subject, tekstveld)

server = smtplib.SMTP(smtp_server, port)
server.sendmail(sender_email, receiver_email, message)
server.quit()
