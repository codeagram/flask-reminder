from .. import db
from ..models import User, Reminder
from secrets import token_hex
from datetime import datetime
import requests
import socket


class SendReminder:

    def get_reminders(self):

        sendable_reminders = []
        total_reminders = db.session.query(Reminder).all()
        time_now = datetime.now()

        for reminder in total_reminders:
            if reminder.due_date < time_now and reminder.is_active == True:
                rem = {'sender': reminder.sender,
                        'receiver': reminder.receiver.name,
                        'content': reminder.content,
                        'key': reminder.unique_key}
                sendable_reminders.append(rem)

        return sendable_reminders

    def send_reminders(self):

        sendable_reminders = self.get_reminders()
        telegram = Telegram()

        base_url = socket.getfqdn()

        for reminder in sendable_reminders:

            key = reminder['key']

            link = f"{base_url}/{key}"

            message = """\
A reminder from {}, Regarding \'{}\'.
Use {} to reschedule the reminder.
""".format(reminder['sender'],
            reminder['content'],
            link)
            chat_id = get_chat_id(reminder['receiver'])
            telegram.send_message(chat_id, message)
            reupdate(key)


def get_chat_id(name):

    user = User.query.filter_by(name=name).first()
    chat_id = user.telegram_id

    return chat_id


class Telegram:

    def __init__(self):

        self.url = "https://api.telegram.org/bot1770514264:AAFfu4-CEYiXi1vHPdtGihN2O-mGb_rcY40"

    def send_message(self, chat_id, message):

        base_url = f"{self.url}/sendMessage?chat_id={chat_id}&text={message}"
        response = requests.get(base_url)

        return response


def reupdate(RemKey):

    reminder = Reminder.query.filter_by(unique_key=RemKey).first()
    reminder.is_active = False

    db.session.add(reminder)
    db.session.commit()
