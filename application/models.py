from datetime import datetime
from secrets import token_hex
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from application import db, login


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, unique=True)
    telegram_id = db.Column(db.String(32), index=True, unique=True)
    reminders_list = db.relationship('Reminder', backref='receiver',     lazy='dynamic')

    def __init__(self, name, telegram_id):

        self.name = name
        self.telegram_id = telegram_id

    def __repr__(self):

        return f"<User: {self.name}"


class Reminder(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(20))
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    content = db.Column(db.String(1024))
    due_date = db.Column(db.DateTime, index=True)
    unique_key = db.Column(db.String(16), index=True, unique=True)
    is_active = db.Column(db.Boolean, index=True, default=True)
    created_on = db.Column(db.DateTime, index=True, default=datetime.    now)

    def __init__(self, sender, receiver, content, due_date):

        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.due_date = due_date

    def set_unique_key(self):

        self.unique_key = tokenhex(8)

    def __repr__(self):

        return f"<Reminder sender:{self.sender}, receiver:{self.receiver_id}"


class Administrator(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, username):

        self.username = username

    def __repr__(self):

        return f"<Admin: {self.username}>"

    def set_password(self, password):

        self.password_hash = generate_password_hash(password)

    def check_password_hash(self, password):

        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):

    return Administrator.query.get(int(id))


#db.create_all()


def user_pollute():

    users = User.query.all()

    user_list = [
            ['Arunkumar', '792670289'],
            ['Vasanth', '393566976'],
            ['Gowsalya', '1063670032'],
            ['Dhandapani', '546382498'],
            ['Sivakumar', '1182946193'],
            ]

    if len(users) == 0:
        for user in user_list:
            u = User(name=user[0], telegram_id=user[1])
            db.session.add(u)

        db.session.commit()

    db.session.close()


def admin_pollute():

    admins = Administrator.query.all()

    administrator = "admin"

    if len(admins) == 0:
        a = Administrator(username="root")
        db.session.add(a)
        a.set_password("admin")
        db.session.commit()

    db.session.close()


#user_pollute()
#admin_pollute()
