from flask import Blueprint, render_template


simon = Blueprint("simon_game", __name__)


@simon.route("/simon_game")
def simon_app():
    return render_template("/simon/simon_game.html")
