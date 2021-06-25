from . import auth_bp
from ..admin import admin_bp
from .forms import LoginForm
from flask import render_template, request, redirect, url_for, flash
from flask_login  import login_required, login_user, logout_user, current_user
from application.models import Administrator
from werkzeug.urls import url_parse


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('admin_bp.admin'))

    form = LoginForm()

    if form.validate_on_submit():
        user = Administrator.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password_hash(form.password.data):

            flash('Invalid Username or Password')
            return redirect(url_for("auth_bp.login"))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("auth_bp.login")

        return redirect(next_page)

    return render_template("login.html", form=form)
