from flask import render_template, request, Blueprint
from website.blog.models import BlogPost

core = Blueprint("core", __name__)


@core.route("/blog/")
def index():
    page = request.args.get("page", 1, type=int)
    blog_post = BlogPost.query.order_by(BlogPost.date.desc()).paginate(
        page=page, per_page=5
    )
    return render_template("index.html", blog_post=blog_post)


@core.route("/blog/info")
def info():
    return render_template("info.html")
