from email.mime.text import MIMEText
import smtplib

def send_email(name, email, message):
    from_email="example@gmail.com"
    from_password="vtowzzsuzxxxxxys"
    to_email=email

    subject="Database Web App"
    message="Hey <strong>%s</strong>, you entered this email address '<strong>%s</strong>' and we got your message as '<strong>%s</strong>' . <br> Thanks for reaching out to us!" % (name, email, message)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
