from . import AuthBP
from .models import User
from .forms import LoginForm
from flask_login import login_user, current_user
from flask import render_template, redirect, url_for, flash


@AuthBP.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        if current_user.team == "Collections":
            return redirect(url_for("SpareKeyBP.collections"))
        else:
            return redirect(url_for("SpareKeyBP.index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid Username or Password", "error")
            return redirect(url_for("AuthBP.login"))
        login_user(user, remember=form.remember_me.data)
        if user.team == "Collections":
            return redirect(url_for("SpareKeyBP.collections"))
        else:
            return redirect(url_for("SpareKeyBP.index"))


    return render_template("login.html", form=form)
