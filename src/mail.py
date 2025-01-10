import smtplib

email_sender = 'soumyadiperikson@gmail.com'
email_password = 'soumyadipsikdar'
email_reciever = 'xavierianshreya@gmail.com'

subject = 'Calling out to my better half'
body = "Remember i'll always love you no matter what"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login(email_sender,'ciuckkdegptfrilg')
server.sendmail(email_sender,email_reciever,body)

print("email has been sent")