# send_email.py
import os
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

def send_email():
    msg = MIMEText(f"This is an automated email sent at {datetime.utcnow()} UTC.")
    msg['Subject'] = 'Automated Email'
    msg['From'] = os.environ['EMAIL_USER']
    msg['To'] = os.environ['EMAIL_TO']

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.environ['EMAIL_USER'], os.environ['EMAIL_PASS'])
        smtp.send_message(msg)

if __name__ == '__main__':
    send_email()
