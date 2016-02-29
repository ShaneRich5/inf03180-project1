from app import app, db
from flask import render_template, request, url_for
from app.models import User 
from app.forms import UserForm

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/profile', methods=['GET', 'POST'])
def new_profile():
	form = UserForm()
	return render_template('new_profile.html', form=form)

@app.route('/profiles', methods=['GET', 'POST'])
def all_profiles():

	return render_template('list_profiles.html')

@app.route('/profile/<userid>', methods=['GET', 'POST'])
def show_profile(userid):
	return render_template('show_profile.html')

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'