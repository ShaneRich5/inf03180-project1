from app import app
from flask import render_template, request, url_for


@app.route('/')
def home():
	return render_template('home.html')


@app.route('/profile', methods=['GET', 'POST'])
def new_profile():
	return render_template('new_profile.html')

@app.route('/profiles', methods=['GET', 'POST'])
def all_profiles():
	return render_template('list_profiles.html')

@app.route('/profile/<userid>', methods=['GET', 'POST'])
def show_profile(userid):
	return render_template('show_profile.html')