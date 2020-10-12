from flask import Blueprint, render_template, redirect, url_for


drumkit = Blueprint("drum", __name__)


@drumkit.route("/drums")
def drum_app():
    return render_template("/drum-kit/index.html")
