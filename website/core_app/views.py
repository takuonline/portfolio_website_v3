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


    #project portifolio

@core_app.route("/natours")
def natours():
    return render_template("./website_portfolio/natours/index.html")


@core_app.route("/trillo")
def trillo():
    return render_template("./website_portfolio/trillo/index.html")
