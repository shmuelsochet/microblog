from flask_mail import Message
from flask import render_template
from app import mail, app


def send_email(subject, sender, recipients, cc, bcc, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients, cc=cc,
                  bcc=bcc)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset your password',
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               cc=app.config['ADMINS'][0],
               bcc=app.config['ADMINS'][0],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token)
               )
