from flask import render_template

from app import app
from app.email import send_email


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset your password',
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               cc=[app.config['ADMINS'][0]],
               bcc=[app.config['ADMINS'][0]],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token)
               )
