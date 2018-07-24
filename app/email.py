from flask_mail import Message
from flask import render_template, current_app
from app import mail
from threading import Thread


def send_async_mail(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, cc, bcc, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients, cc=cc,
                  bcc=bcc)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_mail, args=(current_app._get_current_object(), msg)).start()


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset your password',
               sender=current_app.config['ADMINS'][0],
               recipients=[user.email],
               cc=[current_app.config['ADMINS'][0]],
               bcc=[current_app.config['ADMINS'][0]],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token)
               )
