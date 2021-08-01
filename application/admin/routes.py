from . import AdminBP
from flask import Flask, render_template, redirect, url_for, flash
from .forms import ChangeSetting, AddFieldOfficer
from .models import Settings, FieldOfficer


@AdminBP.route("/settings", methods=["GET", "POST"])
def settings():

    change_setting_form = ChangeSetting()
    add_field_officer = AddFieldOfficer()

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
        field_officer.add_a_field_officer(name)

        flash("Field Officer Added", "success")

        return redirect(url_for("AdminBP.settings"))

    return render_template("settings.html", change_setting_form=change_setting_form, add_field_officer=add_field_officer)
