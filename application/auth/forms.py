from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):

    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")


class ChangePassword(FlaskForm):

    old_password = PasswordField("Old Passoword", validators=[InputRequired()])
    new_password = PasswordField("New Password", validators=[InputRequired()])
    submit = SubmitField("Change Password")
