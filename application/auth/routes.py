from . import AuthBP
from .models import User
from .forms import LoginForm, ChangePassword
from flask_login import login_user, current_user, logout_user, login_required
from flask import render_template, redirect, url_for, flash


@AuthBP.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        if current_user.role == "Collections":
            return redirect(url_for("SpareKeyBP.collections"))
        else:
            return redirect(url_for("SpareKeyBP.index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash("Invalid Username or Password", "danger")

            return redirect(url_for("AuthBP.login"))

        login_user(user, remember=form.remember_me.data)
        if current_user.role == "Collections":
            return redirect(url_for("SpareKeyBP.collections"))
        else:
            return redirect(url_for("SpareKeyBP.index"))

    return render_template("login.html", form=form)


@AuthBP.route("/logout")
def logout():

    logout_user()

    return redirect(url_for("AuthBP.login"))

@AuthBP.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():

    form = ChangePassword()

    if form.validate_on_submit():
        user = User.query.get(current_user.id)
        if user.check_password(form.old_password.data) == True:
            user.change_password(form.old_password.data, form.new_password.data)
            flash("Password Changed Successfully", "success")
        else:
            flash("Error Changing Password, Try Again!", "danger")

        return redirect(url_for("SpareKeyBP.index"))

    return render_template("change_password.html", form=form)


