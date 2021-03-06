from flask_wtf import FlaskForm
from wtforms import SubmitField


class DeleteForm(FlaskForm):

    delete = SubmitField('Delete')


class EditForm(FlaskForm):

    edit = SubmitField("Edit")
