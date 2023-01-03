from wtforms import (
    Form,
    StringField,
    TextAreaField,
    PasswordField,
    validators
)


class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=5, max=40)])
    username = StringField('Username', [validators.Length(min=7, max=30)])
    email = StringField('Email', [validators.Length(min=7, max=35)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Password does not match')
    ])
    confirm = PasswordField('Confirm Password')

