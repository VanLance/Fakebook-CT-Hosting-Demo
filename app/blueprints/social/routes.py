from . import bp as social_bp 
from app.blueprints.social.models import User, Post
from app.forms import PostForm, SearchForm
from flask import redirect, render_template, url_for, flash, g
from flask_login import login_required, current_user
from app import app

@app.before_request
def before_request():
    g.post_form = PostForm()
    g.search_form = SearchForm()

@social_bp.route('/user/<username>')
def user(username):
    user_match = User.query.filter_by(username=username).first()
    if not user_match:
        flash(f'User {username} doesn\'t exit')
        return redirect(url_for('main.index'))
    posts = user_match.posts
    return render_template('user.jinja', user=user_match, posts=posts, search_form=g.search_form, post_form=g.post_form)


@social_bp.post('/post')
@login_required
def post():
    if g.post_form.validate_on_submit():
        body = g.post_form.body.data
        p = Post(body=body, user_id=current_user.id)
        p.commit()
        return redirect(url_for('social.user', username=current_user.username))
    return redirect(url_for('main.index'))
    
@social_bp.post('/search')
def user_search():
    if g.search_form.validate_on_submit():
        return redirect(url_for('social.user',username=g.search_form.username.data))
    return redirect(url_for('main.index'))