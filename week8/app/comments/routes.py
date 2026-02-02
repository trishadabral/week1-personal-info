from flask import redirect, url_for
from flask_login import login_required, current_user
from app.comments import bp
from app.comments.forms import CommentForm
from app.models import Comment
from app import db

@bp.route("/add/<int:post_id>", methods=["POST"])
@login_required
def add_comment(post_id):
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(content=form.content.data, author=current_user, post_id=post_id)
        db.session.add(comment)
        db.session.commit()
    return redirect(url_for("posts.view", id=post_id))
