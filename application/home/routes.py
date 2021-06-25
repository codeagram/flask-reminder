from . import home_bp
from .forms import ReminderForm
from flask import render_template, redirect, url_for, request, flash
from .home import AddReminder, GetArgs, EditReminder


@home_bp.route("/", methods=["GET", "POST"])
def index():

    form = ReminderForm()

    if request.method == "POST":

        if form.validate_on_submit():

            r = GetArgs(form)
            reminder = r.get_args()
            AddReminder(reminder)
            flash("Reminder saved successfully!", "success")

        else:
            flash("Something went wrong, Please resubmit the form", "danger")

        return redirect(url_for("home_bp.index"))

    return render_template("index.html", form=form)


@home_bp.route("/edit/<RemKey>", methods=["GET", "POST"])
def edit(RemKey):

    edit = EditReminder(RemKey)
    reminder = edit.get_reminder()

    return redirect(url_for("home_bp.index", reminder=reminder))
