from flask import render_template, flash, redirect,url_for
from . import bp as app
from app.forms import RegisterForm, SignInForm
from app.blueprints.social.models import User
from flask_login import login_user, logout_user

@app.route('/register', methods=['GET',"POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        
        check_username = User.query.filter_by(username=username).first()
        check_email = User.query.filter_by(email=email).first()
        if check_username:
            flash(f'Username {username} is taken, enter different Username')
        elif check_email:
            flash(f'Email {email} already in use, enter new email')
        else:
            u = User(username=username,email=email,password_hash='')
            u.hash_password(password)
            print(u.password_hash)
            u.commit()
            login_user(u)
            flash(f'Register Requested for {email} {username}','success')
            return redirect('/')
    return render_template('register.jinja', form=form, title='Register')

@app.route('/signin', methods=['GET','POST'])
def sign_in():
    form = SignInForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash(f'{form.username} successfully signed in!')
            return redirect('/')
    return render_template('signin.jinja', sign_in_form=form)

@app.route('/logout')
def log_out():
    logout_user()
    return redirect(url_for('main.index'))