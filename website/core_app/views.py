# website/core/views
from flask import render_template, Blueprint

core_app = Blueprint("core_app", __name__)


@core_app.route("/")
def home():
    return render_template("home.html")


@core_app.route("/about")
def about():
    return render_template("about.html")


@core_app.route("/contact")
def contact():
    return render_template("contact.html")
