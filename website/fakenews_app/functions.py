from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
import joblib
import string
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


def text_process(mess):
    stemmer = PorterStemmer()

    nopunc = [char for char in mess if char not in string.punctuation]

    nopunc = "".join(nopunc)

    no_stop = [
        word
        for word in nopunc.split()
        if word.lower() not in stopwords.words("english")
    ]
    return [stemmer.stem(x) for x in no_stop]
