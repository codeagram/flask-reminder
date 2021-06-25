from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
from flask_login import LoginManager


db = SQLAlchemy()
scheduler = APScheduler()
login = LoginManager()

def init_app():

    app = Flask(__name__)

    if app.config["ENV"] == 'production':
        app.config.from_object('config.ProdConfig')

    else:
        app.config.from_object('config.DevConfig')

    with app.app_context():

        db.init_app(app)
        scheduler.init_app(app)
        login.init_app(app)
        login.login_view = "auth_bp.login"

        from .admin import admin_bp, routes
        from .home import home_bp, routes
        from .auth import auth_bp, routes

        app.register_blueprint(admin_bp)
        app.register_blueprint(home_bp)
        app.register_blueprint(auth_bp)

        #from .tasks.job import send_reminders

    return app
