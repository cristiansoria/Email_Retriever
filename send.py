import smtplib
import os
import imghdr
from email.message import EmailMessage
from email.mime.text import MIMEText
from email import encoders
import config

emails = []

files = ['Cristian_Soria.pdf', 'CV.txt']
text = open("CV.txt").read()
msg = EmailMessage()
msg['Subject'] = 'Internship Opportunities for Students 2020'
msg['From'] = config.EMAIL_ADDRESS
print(text)
msg.set_content(text)
elist = open("Emails.txt")
for line in elist:
    line = line.replace(",", "")
    emails.append(line)
msg['To'] = emails[0]+""

    # msg['To'] = "cristiansoria@csus.edu"

with open(files[0], 'rb') as f:
    file_data = f.read()
    file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename = file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(config.EMAIL_ADDRESS, config.PASSWORD)
    smtp.send_message(msg)