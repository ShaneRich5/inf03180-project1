from . import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(20))
	last_name = db.Column(db.String(20))
	registration_number = db.Column(db.String(10), unique=True)
	gender = db.Column(db.String(10))
	age =db.Column(db.Integer)
	image = db.Column(db.String(80), unique=True)

	def __init__(self, first_name, last_name, registration_number, gender, age, image):
		self.first_name = first_name
		self.last_name = last_name
		self.registration_number = registration_number
		self.gender = gender
		self.age = age 
		self.image = image

	def __repr__(self):
		return '<User %r>' % self.registration_number
