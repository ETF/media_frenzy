from mf_app import db
import datetime


class User(db.Model):

	__tablename__ = "users"

	user_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, unique=True, nullable=False)
	email = db.Column(db.String, unique=True, nullable=False)
	password = db.Column(db.String, nullable=False)
	register_date = db.Column(db.Date)

	def __init__(self, name=None, email=None, password=None, register_date=None):
		self.name = name
		self.email = email
		self.password = password
		if register_date is None:
			register_date = datetime.datetime.utcnow()
		self.register_date = register_date

	def __repr__(self):
		return '<User %r>' % (self.name)