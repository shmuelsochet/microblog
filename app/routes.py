from flask import render_template, flash, redirect, get_flashed_messages
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {
        'username': 'Shmuel'
    }
    posts = [
        {
            'author': user,
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool'
        }
    ]
    return render_template('index.html', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.password.data, form.username.data, form.remember_me.data
        ))

        return redirect('/index')

    return render_template('login.html', title='Sign In', form=form, flash=get_flashed_messages())
