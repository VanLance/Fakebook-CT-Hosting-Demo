from . import bp as social_bp 
from app.blueprints.social.models import User, Post
from app.forms import PostForm, SearchForm
from flask import redirect, render_template, url_for, flash,g
from flask_login import login_required, current_user

@social_bp.route('/user/<username>')
def user(username):
    form=SearchForm()
    form2=PostForm()
    user_match = User.query.filter_by(username=username).first()
    if not user_match:
        flash(f'User {username} doesn\'t exit')
        return redirect(url_for('main.index'))
    posts = user_match.posts
    return render_template('user.jinja', user=user_match, posts=posts, search_form=form, post_form=form2)

@social_bp.post('/post')
@login_required
def post():
    form = PostForm()
    # if g.post_form.validate_on_submit():
    if form.validate_on_submit():
        body = form.body.data
        p = Post(body=body, user_id=current_user.id)
        p.commit()
        return redirect(url_for('social.user', username=current_user.username))
    return redirect(url_for('main.index'))
    
@social_bp.post('/search')
def user_search():
    g.search_form=SearchForm()
    if g.search_form.validate_on_submit():
        return redirect(url_for('social.user',username=g.search_form.username.data))
    return redirect(url_for('main.index'))