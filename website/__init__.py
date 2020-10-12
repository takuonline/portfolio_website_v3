# website/__init__.py
from flask import Flask
from website.dictionary.views import dict_app
from website.core_app.views import core_app
from website.blur_app.views import face_app
from website.fakenews_app.views import news
from website.drumkit.views import drumkit
from website.ml_files.views import ml
from website.simon_game.views import simon

from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_login import LoginManager


################################
#####(Flask app setup)##########
################################

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

################################
#####(Database setup)###########
################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join( basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)

#####################################
######(Blueprint registering)########
#####################################

app.register_blueprint(core_app)
app.register_blueprint(dict_app)
app.register_blueprint(face_app)
app.register_blueprint(news)
app.register_blueprint(drumkit)
app.register_blueprint(ml)
app.register_blueprint(simon)


#####################################
#############(Blog)##################
#####################################

login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.init_app(app)

from website.blog.users.views import users
from website.blog.core.views import core
from website.blog.error_pages.handlers import error_pages
from website.blog.blog_posts.views import blog_posts

# registering blog blueprints

app.register_blueprint(blog_posts)
app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.static_folder = "static"

####################################################################################
