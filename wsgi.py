from application import init_app, scheduler
from application import scheduler, send_reminders


app = init_app()
scheduler.add_job(trigger="interval", id="send", seconds=5, func=send_reminders)
