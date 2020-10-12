from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed


class NewsForm(FlaskForm):
    text = TextAreaField(
        "Please paste the news article below", validators=[DataRequired()]
    )
    submit = SubmitField("Submit")
