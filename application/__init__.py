from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_apscheduler import APScheduler


login = LoginManager()
scheduler = APScheduler()
db = SQLAlchemy()

def init_app():

    app = Flask(__name__)

    if app.config["ENV"] == 'production':
        app.config.from_object('config.ProdConfig')

    else:
        app.config.from_object('config.DevConfig')

    db.init_app(app)
    scheduler.init_app(app)
    scheduler.start()

    def send_reminders():
        A = SendReminder()
        A.send_reminders()
        print('Send Reminders')

    app.app_context().push()

    with app.app_context():

        db.create_all()
        login.init_app(app)
        login.login_view = "auth_bp.login"

        from .admin import admin_bp, routes
        from .home import home_bp, routes
        from .auth import auth_bp, routes

        app.register_blueprint(admin_bp)
        app.register_blueprint(home_bp)
        app.register_blueprint(auth_bp)



    return app


from .task.job import SendReminder

def send_reminders():
    A = SendReminder()
    A.send_reminders()
    print('Send Reminders')
