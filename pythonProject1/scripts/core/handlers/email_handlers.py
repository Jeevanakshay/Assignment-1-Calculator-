import smtplib
from scripts.logging.logger import logger
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from schema.models import Email
from scripts.Execption.execption import EmailHandlerException
from scripts.constants.app_constants import Email_handler


def send_email(body, email: Email):
    sender_email = "jeevanakshay14@gmail.com"
    sender_password = "shrwoflhxtjkepte"
    receiver_email = email.rec_email

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = Email_handler.Subject_obj
    message.attach(MIMEText(body, "html"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)
        server.quit()
        return {Email_handler.message}
    except Exception as e:
        logger.error(EmailHandlerException.EX006.format(error=str(e)))
        return {"message": str(e)}
