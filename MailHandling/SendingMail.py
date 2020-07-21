import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
sender_mail = 'susil.sahoo778@gmail.com'
receiver_mail = 'susil.sahoo78@gmail.com'
mail_content = '''Hello,
This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
Thank You'''
message = MIMEMultipart()
message['From'] = sender_mail
message['To'] = receiver_mail
message['Subject'] = 'A test mail sent by Python. It has an attachment.'
message.attach(MIMEText(mail_content, 'plain'))
try:
    password = "***"
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login(sender_mail, password)
    text = message.as_string()
    smtpObj.sendmail(sender_mail, receiver_mail, message)
    smtpObj.quit()
    print("sending mail to %s successful..." % sender_mail)
except ConnectionError:
    print("sending mail failed to %s" % receiver_mail)
