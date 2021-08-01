from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, IntegerField, HiddenField
from wtforms.validators import InputRequired
from wtforms.fields.html5 import DateField
from application.admin.models import FieldOfficer, get_field_officers


branches = ["1GOB", "2MLR", "3POL", "4CBE", "5TPR", "6ERD", "7DG", "8KRR"]

recepients = [("Collections", "Collections")]

class AddSpareKey(FlaskForm):

    branches_tuple = list()
    for branch in branches:
        branches_tuple.append((branch, branch))

    branch = SelectField("Branch", validators=[InputRequired()], choices=branches)
    today = DateField("Today Date")
    loan_no = StringField("Loan No", validators=[InputRequired(message="Please Enter Loan Number")])
    name = StringField("Name",validators=[InputRequired(message="Please Enter Name")])
    recepient = SelectField("Recepient", choices=recepients)
    remarks = StringField("Remarks")
    submit = SubmitField("Submit")


class AddFieldOfficer(FlaskForm):

    name = StringField("Name", validators=[InputRequired(message="Please Enter a Name")])
    submit = SubmitField("Add")


class ChangeDefaultDays(FlaskForm):

    days = IntegerField("Default Days")


class InwardKey(FlaskForm):

    inward = SubmitField("Inward")
    key_id = HiddenField()


class ReassignKey(FlaskForm):

    field_officers = get_field_officers()
    #field_officers = []

    key_id = HiddenField()
    recepient = SelectField("Recepient", choices=field_officers, validators=[InputRequired(message="Please select recepient")])
    submit = SubmitField("Reassign")
