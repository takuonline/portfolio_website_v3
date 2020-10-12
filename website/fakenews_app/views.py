#! /usr/bin/python3
from website.fakenews_app.functions import text_process
from flask import Flask, render_template, session, redirect, url_for, Blueprint
from flask_wtf import FlaskForm
from website.fakenews_app.forms import NewsForm
import joblib, string, os
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


news = Blueprint("news", __name__)


@news.route("/news_form", methods=("POST", "GET"))
def news_app():

    form = NewsForm()
    full_path = os.path.join("website//static//", "news_classifier.joblib")

    model = joblib.load(full_path)
    y = False  # set flag yto false

    if form.validate_on_submit():
        news = [(form.text.data)]
        y = str(model.predict(news)[0])

        session["y"] = str(model.predict(news)[0])
        session["proba_fake"] = str(model.predict_proba(news)[0][0].round(3))
        session["proba_real"] = str(model.predict_proba(news)[0][1].round(3))

        if y == "1":
            session["y"] = "  Real"
        elif y == "0":
            session["y"] = "  Fake"
        else:
            session["y"] = "Sorry we could not get an answer for you. Please try again"

        # return redirect(url_for("news.news_prediction"))

    return render_template("news_form.html", form=form, y=y)


@news.route("/news_prediction")
def news_prediction():
    return render_template("news_prediction.html")
