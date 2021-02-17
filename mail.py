import smtplib
from homerun_credentials import *
from email.message import EmailMessage


def shoot_mail(subject, body):
    msg = EmailMessage()
    msg['Subject'] = f'Automation Homerun - {subject}'
    msg['From'] = emailAddress
    msg['To'] = send_mail_to
    msg['Reply-to'] = 'sk0196146@gmail.com'
    msg.set_content(f'{body}')

    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(emailAddress, emailPassword)
    s.send_message(msg)
    # terminating the session
    s.quit()
    print("Success")


# shoot_mail("Test", "Hello")
