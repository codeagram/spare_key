from application import db
from datetime import datetime


class spare_key(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    branch = db.Column(db.String(32), nullable=False)
    loan_no = db.Column(db.String(32), nullable=False)
    name = db.Column(db.String(32))
    recepient = db.Column(db.String(32))
    expected_date_of_return = db.Column(db.Date)
    returned_date = db.Column(db.Date)
    remarks = db.Column(db.String(100), default=" ")
    is_active = db.Column(db.Boolean, default=True)
    added = db.Column(db.DateTime, default=datetime.now)
    updated = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    days = db.Column(db.String(32))
