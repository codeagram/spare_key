from . import SpareKeyBP
from flask import Flask, render_template, redirect, url_for, flash, request
from .forms import AddSpareKey, InwardKey, ReassignKey
from sqlalchemy.exc import IntegrityError
from .models import SpareKey, add_spare_key, get_keys_with_field_officers
from datetime import date
from flask_login import login_required, current_user
from ..admin.models import Settings


@SpareKeyBP.route("/")
@login_required
def index():

    if current_user.role == "Collections":
        return redirect(url_for("SpareKeyBP.collections"))

    key = SpareKey()
    pending_keys = key.get_keys_older_than_default_time()

    return render_template("index.html", pending_keys=pending_keys)


@SpareKeyBP.route("/add", methods=["GET", "POST"])
@login_required
def add():

    if current_user.role == "Collections":
        return redirect(url_for("SpareKeyBP.collections"))

    form = AddSpareKey()
    sparekey = SpareKey()

    if form.validate_on_submit():

        is_exists = sparekey.check_key(form.loan_no.data)

        if is_exists == False:

            add_spare_key(branch=form.branch.data,
                        added_date=form.today.data,
                        loan_no=form.loan_no.data.cap,
                        name=form.name.data.title(),
                        recepient=form.recepient.data,
                        remarks=form.remarks.data)
            flash("Successfully Added", "success")
            return redirect(url_for("SpareKeyBP.add"))

        else:
            flash("Allready Found a Key with same Loan Number", "error")
            return redirect(url_for("SpareKeyBP.add"))

    default_days = Settings.query.filter_by(name="Default Days").first()

    return render_template("add.html", form=form, default_days=default_days.value)


@SpareKeyBP.route("/collections", methods=["GET", "POST"])
@login_required
def collections():

    if current_user.role == "Documentation":
        return redirect(url_for("SpareKeyBP.index"))

    inward_form=InwardKey()
    reassign_form=ReassignKey()
    keys = SpareKey()

    if inward_form.validate_on_submit():
        key_id = inward_form.key_id.data
        keys.inward_to_collections(key_id)

        return redirect(url_for("SpareKeyBP.collections"))

    keys = SpareKey()
    all_keys = keys.get_keys_with_collections()

    keys_with_field_officers = get_keys_with_field_officers()

    return render_template("collections.html", all_keys=all_keys, keys_with_field_officers=keys_with_field_officers, inward_form=inward_form, reassign_form=reassign_form)


@SpareKeyBP.route("/reassign", methods=["POST"])
@login_required
def reassign():

    if current_user.role == "Documentation":
        return redirect(url_for("SpareKeyBP.collections"))

    reassign_form=ReassignKey()

    if reassign_form.validate_on_submit():
        key_id = reassign_form.key_id.data
        recepient = reassign_form.recepient.data
        key = SpareKey()
        key.reassign_key(key_id, recepient)

        return redirect(url_for("SpareKeyBP.collections"))

    return redirect(url_for("SpareKeyBP.collections"))


@SpareKeyBP.route("/reports", methods=["GET", "POST"])
@login_required
def reports():

    if current_user.role == "Collections":
        return redirect(url_for("SpareKeyBP.collections"))

    sparekey = SpareKey()
    form=InwardKey()

    all_keys = sparekey.get_all_active_keys()

    if form.validate_on_submit():
        key_id = form.key_id.data
        key = SpareKey()
        key.make_inward(key_id)

        return redirect(url_for("SpareKeyBP.reports"))

    return render_template("reports.html", all_keys=all_keys, form=form)
