from website.blur_app.functions import detect_and_blur_plate
from website.blur_app.forms import FaceForm
from flask import render_template, session, Blueprint, redirect, url_for
import os

face_app = Blueprint("face_app", __name__)


@face_app.route("/face_blur", methods=["GET", "POST"])
def face_blur():
    name = None
    form = FaceForm()
    y = None

    if form.validate_on_submit():
        y = None
        img = form.pic.data
        session["submit"] = form.submit.data

        y = str(detect_and_blur_plate(str(img)))
        dirname = os.path.dirname(__file__)
        website = os.path.join(dirname, "..")
        pic_path = os.path.join(website, "static")

        # getting file from the static folder
        session["name"] = y

        return redirect(url_for("face_app.thankyou"))

    return render_template("face_blur.html", form=form, name=name, y=y)


@face_app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")
