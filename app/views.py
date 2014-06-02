
# -*- coding: utf-8 -*-

from app import app, db
from flask import render_template
from models import Post, User

@app.route('/')
def index():
	all_user = User.query.all()
	all_post = Post.query.all()
	return render_template("Index.html", all_user = all_user, all_post = all_post)
