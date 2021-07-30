from application import db
from .models import spare_key
from datetime import timedelta, datetime


class SpareKey:

    def __init__(self):

        pass

    def add(self, branch, loan_no, name, recepient, expected_date_of_return, remarks):

        key = spare_key(branch=branch,
                        loan_no=loan_no,
                        name=name,
                        recepient=recepient,
                        expected_date_of_return=expected_date_of_return,
                        remarks=remarks)

        db.session.add(key)
        db.session.commit()
        db.session.close()

    def get_all_keys(self):

        all_keys = spare_key.query.filter_by(is_active=True).all()

        db.session.close()

        return all_keys

    def get_pending_keys(self):

        all_keys = self.get_all_keys()
        pending_keys = list()
        for key in all_keys:
            added = key.added
            today = datetime.today()
            if added + timedelta(days=30) <= datetime.today():
                pending_keys.append(key)

        return pending_keys

    def get_keys_with_collections(self):

        all_keys = spare_key.query.filter_by(recepient="Collections", is_active=True).all()

        db.session.close()

        return all_keys

    def get_keys_with_all_field_officers(self):

        all_keys = spare_key.query.filter(spare_key.recepient!="Collections").all()

        keys = []
        for k in all_keys:
            if k.is_active==True:
                keys.append(k)

        db.session.close()

        return keys

    def get_keys_with_a_field_officer(self, field_officer):

        all_keys = spare_key.query.filter_by(recepient=field_officer, is_active=True).all()

        db.session.close()

        return all_keys

    def check_key(self, loan_no):

        key = spare_key.query.filter_by(loan_no=loan_no).all()

        for k in key:
            if k.is_active == True:
                return True

        return False


class MakeInward:

    def __init__(self, key_id):

        self.key_id = key_id

        key = spare_key.query.filter_by(id=self.key_id).first()

        key.is_active = False
        key.inward_date = datetime.today()

        db.session.add(key)
        db.session.commit()
        db.session.close()


class InwardToCollection:

    def __init__(self, key_id):

        self.key_id = key_id

        key = spare_key.query.filter_by(id=self.key_id).first()

        key.recepient = "Collections"
        key.inward_date = datetime.today()

        db.session.add(key)
        db.session.commit()
        db.session.close()


class ReassignKey:

    def __init__(self, key_id, recepient):

        self.key_id = key_id

        key = spare_key.query.filter_by(id=self.key_id).first()

        key.recepient = recepient

        db.session.add(key)
        db.session.commit()
        db.session.close()


class Collections:

    def __init__(self):

        pass

    def all_keys(self):

        keys = spare_key.query.filter_by(recepient="Collections", is_active=True).all()

        db.session.close()

        return keys
