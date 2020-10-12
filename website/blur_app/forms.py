from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    BooleanField,
    SelectField,
    SubmitField,
    RadioField,
    TextAreaField,
)
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed


class FaceForm(FlaskForm):
    pic = StringField("Please enter a url of an image file.", validators=[])
    # pic = FileField("Import picture file", validators=[FileAllowed(["jpg","png",'gif']) ])

    # img_vid=RadioField("Select whether you uploaded an image or a video file",choices=[("img","Image file"),("vid","Video file")])

    submit = SubmitField("Submit")
