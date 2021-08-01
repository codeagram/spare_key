from application import db
from datetime import date, datetime, timedelta
from application.admin.models import Settings


class SpareKey(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    branch = db.Column(db.String(32), nullable=False)
    loan_no = db.Column(db.String(32), nullable=False)
    name = db.Column(db.String(32))
    recepient = db.Column(db.String(32))
    expected_date_of_return = db.Column(db.Date())
    returned_date = db.Column(db.Date)
    remarks = db.Column(db.String(100), default=" ")
    is_active = db.Column(db.Boolean, default=True)
    added = db.Column(db.Date, default=date.today)
    updated = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    days = db.Column(db.Date())

    def update_days(self):

        keys = self.query.filter_by(is_active=True).all()
        today = datetime.now()
        for key in keys:
            day_time = key.added - today
            key.days = day_time.days

    def get_all_active_keys(self):

        active_keys = self.query.filter_by(is_active=True).all()

        db.session.close()

        return active_keys

    def get_all_inactive_keys(self):

        inactive_keys = self.query.filter_by(is_active=False).all()

        db.session.close()

        return inactive_keys

    def get_keys_older_than_default_time(self):

        default_time = Settings.query.filter_by(name="Default Days").first()

        keys = self.query.filter_by(self.days>=default_time.value).all()

        db.session.close()

        return keys

    def get_keys_with_collections(self):

        all_keys = self.query.filter_by(recepient="Collections", is_active=True).all()

        db.session.close()

        return all_keys

    def get_keys_with_all_field_officers(self):

        all_keys = self.query.filter(self.recepient!="Collections").all()

        keys = []
        for k in all_keys:
            if k.is_active==True:
                keys.append(k)

        db.session.close()

        return keys

    def get_keys_with_a_field_officer(self, field_officer):

        all_keys = self.query.filter_by(recepient=field_officer, is_active=True).all()

        db.session.close()

        return all_keys

    def check_key(self, loan_no):

        key = self.query.filter_by(loan_no=loan_no).all()

        for k in key:
            if k.is_active == True:
                return True

        return False


    def make_inward(self, key_id):

        key = self.query.filter_by(id=key_id).first()

        key.is_active = False
        key.inward_date = datetime.today()

        db.session.add(key)
        db.session.commit()
        db.session.close()

    def reassign_key(self, key_id, recepient):

        key = self.query.filter_by(id=key_id).first()

        key.recepient = recepient

        db.session.add(key)
        db.session.commit()
        db.session.close()

    def inward_to_collections(self, key_id):

        key = self.query.filter_by(id=key_id).first()

        key.recepient = "Collections"
        key.inward_date = datetime.today()

        db.session.add(key)
        db.session.commit()
        db.session.close()


def add_spare_key(branch, loan_no, name, recepient, remarks, added_date=None):

    print(type(added_date))
    if added_date == None:
        added_date = date.today()

    default_time = Settings.query.filter_by(name="Default Days").first()
    expected_date_of_return = added_date + timedelta(int(default_time.value))

    key = SpareKey(branch=branch,
                   loan_no=loan_no,
                   name=name,
                   recepient=recepient,
                   remarks=remarks,
                   added=added_date,
                   expected_date_of_return=expected_date_of_return
                   )

    db.session.add(key)
    db.session.commit()
    db.session.close()


def get_keys_with_field_officers():

    all_keys = SpareKey.query.filter(SpareKey.recepient!="Collections").all()

    keys = list()

    for k in all_keys:
        if k.is_active == True:
            keys.append(k)

    return keys
