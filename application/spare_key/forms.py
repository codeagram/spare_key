from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField, HiddenField
from wtforms.validators import InputRequired
from wtforms.fields.html5 import DateField
#from .functions import get_recepients


branches = ["1GOB", "2MLR", "3POL", "4CBE", "5TPR", "6ERD", "7DG", "8KRR"]
#recepients = get_recepients()

recepients = [("Collections", "Collections")]

class AddSpareKey(FlaskForm):

    branches_tuple = list()
    for branch in branches:
        branches_tuple.append((branch, branch))

    print(branches_tuple)

    branch = SelectField("Branch", validators=[InputRequired()], choices=branches)
    loan_no = StringField("Loan No", validators=[InputRequired(message="Please Enter Loan Number")])
    name = StringField("Name",validators=[InputRequired(message="Please Enter Name")])
    recepient = SelectField("Recepient", choices=recepients)
    expected_date_of_return = DateField("Expected Date of Return", format="%Y-%m-%d", validators=[InputRequired()])
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

    field_officers = [("", "Select"),("Rajkumar", "Rajkumar"), ("Kalidhas", "kalidhas"), ("Mani", "Mani")]
    recepient = SelectField("Recepient", choices=field_officers, validators=[InputRequired(message="Please select recepient")])
    submit = SubmitField("Reassign")
    key_id = HiddenField()
