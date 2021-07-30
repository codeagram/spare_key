from . import SpareKeyBP
from flask import Flask, render_template, redirect, url_for, flash
from .forms import AddSpareKey, InwardKey, ReassignKey
from .methods import SpareKey, MakeInward, InwardToCollection, Collections
from sqlalchemy.exc import IntegrityError


@SpareKeyBP.route("/")
def index():

    key = SpareKey()
    pending_keys = key.get_pending_keys()

    return render_template("index.html", pending_keys=pending_keys)


@SpareKeyBP.route("/add", methods=["GET", "POST"])
def add():

    form = AddSpareKey()

    if form.validate_on_submit():

        try:
            sparekey = SpareKey()
            sparekey.add(branch=form.branch.data,
                        loan_no=form.loan_no.data,
                        name=form.name.data,
                        recepient=form.recepient.data,
                        expected_date_of_return=form.expected_date_of_return.data,
                        remarks=form.remarks.data)
            print(form.branch.data)

        except IntegrityError:
            flash("Already Found!", "danger")

        else:

            flash("Successfully Added", "success")

        return redirect(url_for("SpareKeyBP.add"))

    return render_template("add.html", form=form)


@SpareKeyBP.route("/collections", methods=["GET", "POST"])
def collections():

    inward_form=InwardKey()
    reassign_form=ReassignKey()

    if inward_form.validate_on_submit():
        key_id = inward_form.key_id.data
        #inward = InwardToCollection(key_id)

        return redirect(url_for("SpareKeyBP.collections"))


    if reassign_form.is_submitted():
        print(reassign_form.errors)
        print("Submitted")
    if reassign_form.validate_on_submit():
        print("True")
        key_id = reassign_form.key_id.data
        print(key_id)
        recepient = reassign_form.recepient.data
        #ReassignKey(key_id, recepient)

        return redirect(url_for("SpareKeyBP.collections"))

    keys = Collections()
    all_keys = keys.all_keys()


    return render_template("collections.html", all_keys=all_keys, inward_form=inward_form, reassign_form=reassign_form)


@SpareKeyBP.route("/reports", methods=["GET", "POST"])
def reports():

    sparekey = SpareKey()
    form=InwardKey()

    all_keys = sparekey.get_all_keys()

    if form.validate_on_submit():
        key_id = form.key_id.data
        inward = MakeInward(key_id)

        return redirect(url_for("SpareKeyBP.reports"))

    return render_template("reports.html", all_keys=all_keys, form=form)
