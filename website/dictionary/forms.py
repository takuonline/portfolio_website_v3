from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed


class DictForm(FlaskForm):
    word = TextAreaField("Please enter a word below")
    submit = SubmitField("Submit")
