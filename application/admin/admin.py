from ..models import db, Reminder, User, Administrator


def get_all_reminders():

    reminders = Reminder.query.filter_by(is_active=True)

    return reminders


def delete_reminder(reminder_id):

    reminder = Reminder.query.filter_by(id=reminder_id).first()

    reminder.is_active = False

    db.session.add(reminder)
    db.session.commit()
    db.session.close()

