from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.models import Post
from app import db

posts = Blueprint("posts", __name__, url_prefix="/posts")

@posts.route("/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        post = Post(title=title, content=content, author=current_user)
        db.session.add(post)
        db.session.commit()

        return redirect(url_for("main.index"))

    return render_template("posts/create.html")


@posts.route("/<int:post_id>")
def view(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("posts/view.html", post=post)
