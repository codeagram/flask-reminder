from ..models import Reminder, User
from application import db


class AddReminder:

    def __init__(self, reminder):

        self.reminder = reminder

        self.unpack_reminders()

    def unpack_reminders(self):

        sender = self.reminder[0]
        receivers = self.reminder[1]
        content = self.reminder[2]
        due_date = self.reminder[3]

        self.add_reminder(sender, receivers, content, due_date)

    def add_reminder(self, sender, receivers, content, due_date):

        for user in receivers:
            receiver = self.get_receiver(user)
            reminder = Reminder(sender, receiver, content, due_date)
            db.session.add(reminder)

        db.session.commit()
        db.session.close()

    def get_receiver(self, name):

        user = User.query.filter_by(name=name).first()

        db.session.close()

        return user


class EditReminder:

    def __init__(self, RemKey):

        self.RemKey = RemKey

    def get_reminder(self):

        reminder = Reminder.query.filter_by(unique_key=RemKey).first()

        return reminder


class GetArgs:

    def __init__(self, form):

        self.form = form

    def get_args(self):

        reminder = []
        reminder.append(self.form.sender.data)
        reminder.append(self.form.receiver.data)
        reminder.append(self.form.content.data)
        reminder.append(self.form.reminder_datetime.data)

        print(reminder)

        return reminder


class GetUsers:

    def __init__(self):

        self.users = db.session.query(User).all()

    def get_users(self):

        users = []
        for user in self.users:
            u = (user.name, user.name)
            users.append(u)

        return users
