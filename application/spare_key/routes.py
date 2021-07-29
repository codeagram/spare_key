from . import SpareKeyBP
from flask import Flask, render_template, redirect, url_for, flash
from .forms import AddSpareKey
from .methods import SpareKey
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

        except IntegrityError:
            flash("Already Found!", "danger")

        flash("Successfully Added", "success")

        return redirect(url_for("SpareKeyBP.add"))

    return render_template("add.html", form=form)


@SpareKeyBP.route("/edit")
def edit():

    return "Edit"


@SpareKeyBP.route("/reports")
def reports():

    sparekey = SpareKey()

    all_keys = sparekey.get_all_keys()

    return render_template("reports.html", all_keys=all_keys)
