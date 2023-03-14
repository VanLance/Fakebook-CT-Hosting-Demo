from . import bp as app
from flask import Flask, render_template
from app.forms import SearchForm, PostForm

@app.route('/')
def index():
    form = SearchForm()
    form2 = PostForm()
    cdn={
        'instructors':('lucas','dylan'),
        'students':['blane','ashmika','abe','zi','connor','martin','noah','erm']
    }
    return render_template('index.jinja', cdn=cdn, title='Home',search_form=form, post_form=form2)

@app.route('/about')
def about():
    form = SearchForm()
    form2 = PostForm()
    return render_template('about.jinja',search_form=form, post_form=form2)