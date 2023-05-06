from . import bp as app
from flask import Flask, render_template, g

@app.route('/')
def index():
    cdn={
        'instructors':('lucas','dylan'),
        'students':['blane','ashmika','abe','zi','connor','martin','noah','erm']
    }
    return render_template('index.jinja', cdn=cdn, title='Home',search_form=g.search_form, post_form=g.post_form)

@app.route('/about')
def about():
    return render_template('about.jinja',search_form=g.search_form, post_form=g.post_form)