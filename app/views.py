
# -*- coding: utf-8 -*-

from app import app, db
from flask import render_template
from models import Post, User
from forms import NewUserForm

@app.route('/')
def index():
	all_user = User.query.all()
	all_post = Post.query.all()
	return render_template("Index.html", all_user = all_user, all_post = all_post)

@app.route('/add_user', methods = ['GET', 'POST'])
def add_user():
	form = NewUserForm()
	if form.validate_on_submit():
		user = User()
		form.populate_obj(user)
		db.session.add(user)
		db.session.commit()
		return redirect('/new_post')
	return render_template("add_user.html", form = form)

@app.route('/new_post')
def new_post():
	return render_template('new_post')
