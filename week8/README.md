# Week 8 Flask Blog Project

A personal blog built with Flask featuring authentication, posts, and comments.

## Features
- User registration/login/logout
- Create, edit, delete blog posts
- Comment on posts
- SQLite database
- Bootstrap responsive design

## Run Locally
pip install -r requirements.txt
flask db init
flask db migrate -m "init"
flask db upgrade
python run.py
