from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length
from wtforms.fields.html5 import DateTimeLocalField
from .home import GetUsers


class ReminderForm(FlaskForm):

    users = GetUsers()
    choices = users.get_users()

    sender = StringField('Name', validators=[InputRequired(), Length(min=1, max=20)])
    receiver = SelectMultipleField('Recipient', choices=choices, validators = [InputRequired()])
    content = TextAreaField('Message', validators=[InputRequired(), Length(min=1, max=1024)])
    reminder_datetime = DateTimeLocalField('Select Date and Time', format='%Y-%m-%dT%H:%M', validators=[InputRequired()])
    submit = SubmitField('Submit')
