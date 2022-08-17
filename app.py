#!/usr/bin/python3

from flask import Flask, render_template, redirect, url_for, abort
import random

from .decorators import welcome_screen
from .post_models import create_post_table, get_posts, find_post, random_post

app = Flask(__name__)

######## SET THE SECRET KEY ###############
# You can write random letters yourself or 
# Go to https://randomkeygen.com/ and select a random secret key
####################
app.secret_key = 'UIe3i39'

with app.app_context():
    create_post_table()

@app.route('/')
@welcome_screen
def home_page():
    return render_template('page.html', posts=get_posts())

@app.route('/welcome')
def welcome_page():
    return render_template('welcome.html')

@app.route('/<post_link>')
@welcome_screen
def post_page(post_link):
    post = find_post(post_link)
    if post:
        return render_template('post.html', post=post)
    else:
        abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

@app.route('/random')
def random_post_page():
    post = random_post()
    return redirect(url_for('post_page', post_link=post['permalink']))
