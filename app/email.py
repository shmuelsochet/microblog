from flask_mail import Message
from app import mail


def send_mail(subject, sender, recipients, cc, bcc, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients, cc=cc,
                  bcc=bcc)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)
