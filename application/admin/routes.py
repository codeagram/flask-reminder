from . import admin_bp
from .forms import DeleteForm, EditForm
from .admin import get_all_reminders, delete_reminder
from flask import request, redirect, url_for, render_template, flash
from flask_login  import login_required, login_user, logout_user, current_user


@admin_bp.route("/admin", methods=["GET", "POST"])
@login_required
def admin():

    if current_user.is_anonymous:
        return redirect(url_for("login"))

    delete_form = DeleteForm()
    edit_form = EditForm()

    reminders = get_all_reminders()

    if delete_form.validate_on_submit():
        reminder_id = request.form.get("reminder_to_delete")
        delete_reminder(reminder_id)

        flash("Reminder Deleted!")
        return redirect(url_for("admin_bp.admin"))

    if edit_form.validate_on_submit():
        reminder_id = edit_form.edit.data
        edit_reminder(reminder_id)

        flash("Reminder Updated Successfully!")
        return redirect(url_for("admin_bp.admin"))

    return render_template("admin.html",
                           reminders=reminders,
                           edit_form=edit_form,
                           delete_form=delete_form)
