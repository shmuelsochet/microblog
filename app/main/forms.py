from flask_wtf import FlaskForm
from wtforms import (
    StringField, SubmitField, TextAreaField
)
from wtforms.validators import (
    DataRequired, ValidationError, Length
)
from flask_babel import lazy_gettext as _1, _
from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField(_1('Username', validators=[DataRequired()]))
    about_me = TextAreaField(_1('About me', validators=[Length(min=0, max=140)]))
    submit = SubmitField(_1('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))


class PostForm(FlaskForm):
    post = TextAreaField(_1('Say something',
                         validators=[DataRequired(), Length(min=1, max=140)]))
    submit = SubmitField(_1('Submit'))

