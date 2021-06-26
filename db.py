from application import db
from application.models import Reminder


rem = Reminder.query.all()
for r in rem:
    print(r.sender, r.receiver.name)
