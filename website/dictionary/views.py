from flask import render_template, Blueprint
from website.dictionary.forms import DictForm
import json
import os
from difflib import get_close_matches

dict_app = Blueprint("dict", __name__)


@dict_app.route("/dict", methods=["GET", "POST"])
def dictionary():
    form = DictForm()

    meaning = False
    no_meaning = False
    y = False
    other_word = False

    if form.validate_on_submit():

        word = form.word.data
        form.word.data = ""
        dirname = os.path.dirname(__file__)
        website = os.path.join(dirname, "..")
        data_folder = os.path.join(website, "static", "data.json")

        data = json.load(open(data_folder))
        word = word.lower().strip()

        if word in data:
            meaning = data[word]
        else:
            other_word = get_close_matches(word, data.keys(), n=1)
            if other_word == []:
                no_meaning = True
                meaning = True

            else:
                y = True
                no_meaning = True
                other_word = other_word[0]

    return render_template(
        "dict.html",
        form=form,
        meaning=meaning,
        other_word=other_word,
        no_meaning=no_meaning,
        y=y,
    )
