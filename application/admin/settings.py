from application import db
from .models import Settings

def change_a_setting(name, value):

    setting = Setting.query.filter_by(name=name).first()

    setting.change_setting(value)

    db.session.close()


def add_a_setting(name, value):

    setting = Setting(name=name, value=value)
    db.session.add(setting)
    db.session.commit()
    db.session.close()


def get_setting_names():

    settings = Settings.query.all()

    setting_names = list()
    for setting in settings:
        setting_names.append((setting.name, setting.name))

    db.session.close()

    return setting_names
