import re
from email.mime.text import MIMEText
import config
import smtplib
import os
import imghdr
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email import encoders

emails = []
text = open("CV.txt").read()
msg = EmailMessage()
msg['Subject'] = 'Internship Opportunities for Students'
msg['From'] = '$EMAIL'
msg.set_content(text)
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login("$EMAIL", "$PASSWORD")
elist = open("Emails.txt")
with open('$RESUME', 'rb') as f:
    file_data = f.read()
    file_name = f.name
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename = file_name)

for line in elist:
    line = line.replace(",", "")
    emails.append(line)
for row in emails:
    # print(row)    
    try:
        server.sendmail('$EMAIL', row, msg.as_string())
    except:
        print("error")
server.quit()