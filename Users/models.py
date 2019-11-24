from setup import db, login_manager
from flask_login import UserMixin

class Users(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	password = db.Column(db.String(512), nullable=False)
	dob = db.Column(db.DateTime, nullable=False)
	email = db.Column(db.String(512), unique=True)
	name = db.Column(db.String(512), nullable=False)
	phone = db.Column(db.String(10), nullable=False, unique=True)
	image = db.Column(db.String(512))
	role = db.Column(db.String(128))

	def __init__(self, password, dob, email, name, phone, image, role):
		self.password = password
		self.dob = dob
		self.email = email
		self.name = name
		self.phone = phone
		self.image = image
		self.role = role

	@login_manager.user_loader
	def load_user(user_id):
		return Users.query.get(int(user_id)) 

	def __repr__(self):
		return '<User %r>' % self.name
