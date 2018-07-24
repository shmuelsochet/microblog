from app import db, cli, create_app
from app.models import User, Post

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Post': Post
    }


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.run(debug=True)
