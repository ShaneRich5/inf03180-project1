from app import app, db
from flask import render_template, request, url_for
from werkzeug import secure_filename
from app.models import User 
from app.forms import UserForm

import os
from random import randint

@app.route('/')
def home():
	""" Render the home page """
	return render_template('home.html')

@app.route('/profile', methods=['GET', 'POST'])
def new_profile():
	if request.method == 'GET':
		""" display user form here """
		form = UserForm()
		return render_template('new_profile.html', form=form)
	elif request.method == 'POST':
		first_name = request.form['first_name']
		last_name = request.form['last_name']
		gender = request.form['gender']
		userid = generate_id()
		age = request.form['age']
		image = request.files['image']

		filename = image.filename
		image.save(os.path.join("filefolder", filename))

		# user = User(first_name, last_name, userid, 'M', 21, )
		return first_name
		# return render_template('show_profile.html')

@app.route('/profiles', methods=['GET', 'POST'])
def all_profiles():
	users = User.query.all()

	if request.method == 'GET':
		return render_template('list_profiles.html', users=users)
	elif request.method == 'POST':
		# return json
		return None

@app.route('/profile/<userid>', methods=['GET', 'POST'])
def show_profile(userid):
	if request.method == 'GET':
		return render_template('show_profile.html')
	elif request.method == 'POST':
		# return json
		return None

@app.after_request
def add_header(response):
	"""
	Add headers to both force latest IE rendering engine or Chrome Frame,
	and also to cache the render page for 10 minutes.
	"""
	response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
	response.headers['Cache-Control'] = 'public,max-age=600'
	return response

@app.errorhandler(404)
def page_not_found(error):
	""" Custom 404 page. """
	return "404"
	# uncomment this whenever i make it lol
	# return render_template('404.html'), 404

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

def generate_id():
	return 620000000 + randint(0, 99999)