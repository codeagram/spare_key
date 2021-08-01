from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, PasswordField
from wtforms.validators import InputRequired
from .settings import get_setting_names


class AddSetting(FlaskForm):

    name = StringField("Name of the Setting", validators=[InputRequired()])
    value = StringField("Value", validators=[InputRequired()])
    submit = SubmitField("Add")


class ChangeSetting(FlaskForm):

    #setting_names = get_setting_names()
    setting_names = [("Default Days", "Default Days")]

    name = SelectField("Select a setting to change", choices=setting_names, validators=[InputRequired()])
    value = StringField("value", validators=[InputRequired()])
    submit = SubmitField("Change")


class AddFieldOfficer(FlaskForm):

    name = StringField("Name of the Field Officer", validators=[InputRequired(message="Please enter the Name")])
    submit = SubmitField("Add")


class AddUser(FlaskForm):

    roles = [("Admin", "Admin"), ("Documentation", "Documentation"), ("Collections", "Collections")]
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    role = SelectField("Role", validators=[InputRequired()], choices=roles)
    submit = SubmitField("Add")
