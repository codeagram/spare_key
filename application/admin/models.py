from flask_sqlalchemy import SQLAlchemy
from application import db


class Settings(db.Model):

    """
        Settings Model => Add default days.,etc
    """

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(128))
    value =db.Column(db.String(128))

    def add_new_setting(self, setting_name, setting_value):

        self.name = setting_name
        self.change_setting(setting_value)

    def change_setting(self, setting_value):

        self.value = setting_value
        db.session.add(self)
        db.session.commit()
        db.session.close()

    def add_setting(self):

        self.name = "Default Days"
        self.name = 30


class FieldOfficer(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    def add_a_field_officer(self, name):

        self.name = name
        db.session.add(self)
        db.session.commit()
        db.session.close()

    def delete_a_field_officer(self, name):

        fo = self.query.filter_by(name=name).first()
        db.session.delete(fo)
        db.session.commit()
        db.session.close()

    def get_all_field_officers(self):

        fo = self.query.all()

        db.session.close

        return fo

def get_field_officers():

    fo = FieldOfficer()
    field = fo.get_all_field_officers()
    field_officers = ["Select"]

    for f in field:
        field_officers.append(f.name)

    return field_officers
