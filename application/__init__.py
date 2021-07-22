from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_apscheduler import APScheduler


app = Flask(__name__)
login = LoginManager(app)
login.login_view = "auth_bp.login"
scheduler = APScheduler(app)
db = SQLAlchemy(app)


if app.config["ENV"] == 'production':
    app.config.from_object('config.ProdConfig')

else:
    app.config.from_object('config.DevConfig')


def send_reminders():
    A = SendReminder()
    A.send_reminders()
    print('Send Reminders')

app.app_context().push()

with app.app_context():

    db.create_all()

    from .admin import admin_bp, routes
    from .home import home_bp, routes
    from .auth import auth_bp, routes

    app.register_blueprint(admin_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)


from .task.job import SendReminder

def send_reminders():
    A = SendReminder()
    A.send_reminders()
    print('Send Reminders')


#scheduler.add_job(trigger="interval", id="send", seconds=5, func=send_reminders)
#scheduler.start()
