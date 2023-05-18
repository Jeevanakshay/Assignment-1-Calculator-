import smtplib
from pydantic import BaseModel
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from schema.models import Email


def send_email(body: str, email: Email):
    sender_email = "jeevanakshay14@gmail.com"
    sender_password = "shrwoflhxtjkepte"
    receiver_email = email.rec_email

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "sent email"
    message.attach(MIMEText(body, "plain"))
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)
        server.quit()
        return {"message": "Email sent successfully"}
    except Exception as e:
        return {"message": str(e)}
