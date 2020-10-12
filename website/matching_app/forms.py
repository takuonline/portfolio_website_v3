from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed


class Matching(FlaskForm):
    text = FileField("Please paste the news article below")
    submit = SubmitField("Submit Pics")
