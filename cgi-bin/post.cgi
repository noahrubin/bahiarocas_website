 #!/usr/bin/python

#------------------------------#
print"Content-type: text/html\n"
print
#------------------------------#

import sys
sys.stderr = sys.stdout
from cgi import FieldStorage
import cgitb
import smtplib as smtp
cgitb.enable()

form = FieldStorage()
name = form.getfirst("name", False)
email = form.getfirst("email", False)
comments = form.getfirst("comments", False)

# username = "bahiarocas@gmail.com"
# passphrase = "Dwaynecoloradoseasoning2016"
# server = smtp.SMTP("smtp.gmail.com", 587)
# server.starttls()
# login = False; sent_mail = False
# while not login:
#     try:
#         server.login(username, passphrase)
#         login = True
#     except Exception as e:
#         pass
# while not sent_mail:
#     try:
#         server.sendmail(username, noahski@benrubin.net, "\n".join([name, email, comments]))
#         sent_mail = True
#     except (SMTPHeloError, SMTPSenderRefused, SMTPDataError) as error:
#         pass
#     except SMTPRecipientsRefused as refused:
#         print """ Issue with recipient of email """
# server.quit()
#
# print """
#     Email sent successfully
# """

print "\n".join([name, email, comments])
