from . import AdminBP
from application import db
from flask import Flask, render_template, redirect, url_for, flash
from .forms import ChangeSetting, AddFieldOfficer, AddUser
from .models import Settings, FieldOfficer
from flask_login import current_user, login_required
from ..auth.models import User


@AdminBP.route("/settings", methods=["GET", "POST"])
@login_required
def settings():

    if current_user.role == "Documentation":
        return redirect(url_for("SpareKeyBP.index"))

    elif current_user.role == "Collections":
        return redirect(url_for("SpareKeyBP.collections"))

    change_setting_form = ChangeSetting()
    add_field_officer = AddFieldOfficer()
    add_user = AddUser()

    if change_setting_form.validate_on_submit():
        name = change_setting_form.name.data
        value = change_setting_form.value.data
        setting = Settings.query.filter_by(name=name).first()
        setting.change_setting(value)

        flash("Settings Changed", "success")

        return redirect(url_for("AdminBP.settings"))

    if add_field_officer.validate_on_submit():
        name = add_field_officer.name.data
        field_officer = FieldOfficer()
        field_officer.add_a_field_officer(name.title())

        flash("Field Officer Added", "success")

        return redirect(url_for("AdminBP.settings"))

    if add_user.validate_on_submit():

        user = User(username=add_user.username.data,
                    role=add_user.role.data)
        user.set_password(add_user.password.data)
        db.session.add(user)
        db.session.commit()
        db.session.close()

        flash("User Added", "success")

        return redirect(url_for("AdminBP.settings"))

    return render_template("settings.html", change_setting_form=change_setting_form, add_field_officer=add_field_officer, add_user=add_user)
