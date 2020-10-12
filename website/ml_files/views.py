# website/core/views
from flask import render_template, Blueprint

ml = Blueprint("ml_files", __name__)


# Logistic
@ml.route("/titanic")
def titanic():
    return render_template("models/titanic-logistic-reg.html")


@ml.route("/logistic_project")
def log_project():
    return render_template("models/Logistic-Regression-Project.html")


# Random forest
@ml.route("/forest_project")
def forest_project():
    return render_template("models/forest-project.html")


# SVM
@ml.route("/svm_project")
def svm_project():
    return render_template("models/svm-project.html")


# k-means


@ml.route("/k-means-project")
def k_means_project():
    return render_template("models/K-Means-project.html")


# nlp
@ml.route("/nlp")
def nlp():
    return render_template("models/nlp.html")


@ml.route("/nlp_project")
def nlp_project():
    return render_template("models/nlp-project.html")


# Recommender
@ml.route("/recommender")
def recommender():
    return render_template("models/recommender.html")


# pca
@ml.route("/pca")
def pca():
    return render_template("models/pca.html")


# tf
@ml.route("/tf")
def tf():
    return render_template("models/tf.html")
