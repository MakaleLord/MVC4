###### EXERCISES ##########
# 
#  Exercise 1: In connection.py
#  Exercise 2: Create table for blog posts
#  Exercise 3: Show the posts from database
#  Exercise 4: Save the sample posts in the database.
#  Bonus: Optimize the insert query to get values directly from the parameter
#
#  Homework 1: Show post from database in the post page as well.
#             In this file, post_models.py
#             - Create a new function with the name find_post with one parameter permalink
#             - Inside find_post, execute the sql query to fetch the post with the given permalink
#             - Use fetchone() to get the post and return it.
#
#             In app.py
#             - Import the find_post function from the post_models.py
#             - Inside post_page, remove the existing for loop
#             - Call find_post() and send post_link as parameter
#             - Add an if condition to check if it returns any post
#             - Inside if, render post.html template, send above post as a template variable.
#
#  Homework 2: Fetch and show a random post from the database
#             In this file, post_models.py
#             - Create a new function named random_post
#             - Inside random_post()
#             - Create a connection to database and get cursor object
#             - Execute the select query to get one random post from database.
#             - Use fetchone() to get the post data and return it
#
#             In app.py
#             - Import the function random_post from post_models.py
#             - Create a new route at /random with a route function random_post_page()
#             - Inside random_post_page()
#             - Call the random_post() function to get a random post.
#             - Use the redirect to go to the post page of above random post.
###########################
from .connection import get_db
from .posts import blog_posts

def create_post_table():
    connection = get_db()
    sql = connection.cursor()
    sql.execute('''
    create table if not exists BlogPosts (
        "PostId" integer primary key autoincrement,
        "Title" Text,
        "Author" Text,
        "Content" Text,
        "Permalink" Text,
        "Tags" Text
    )
    ''')

    posts = get_posts()
    if len(posts) == 0:
        for post in blog_posts:
            insert_post(post)


def insert_post(post):
    connection = get_db()
    sql = connection.cursor()
    post_items = post.values()
    sql.execute('''
        Insert into BlogPosts (Title, Author, Content, Permalink, Tags)
        values(?, ?, ?, ? ,?)
    ''', list(post_items))
    connection.commit()

def get_posts():
    connection = get_db()
    sql = connection.cursor()
    data = sql.execute('''select * from BlogPosts''')
    saved_posts = data.fetchall()
    return saved_posts

def find_post(permalink):
    connection = get_db()
    sql = connection.cursor()
    data = sql.execute('''select * from BlogPosts where permalink = ?''', [permalink])
    post = data.fetchone()
    return post

def random_post():
    connection = get_db()
    sql = connection.cursor()
    data = sql.execute('''select * from BlogPosts order by random() Limit 1''')
    post = data.fetchone()
    return post
