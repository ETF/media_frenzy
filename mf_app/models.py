from mf_app import db
import datetime


class User(db.Model):

	__tablename__ = "users"

	user_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, unique=True, nullable=False) #no real names
	email = db.Column(db.String, unique=True, nullable=False) #ways to authenticate?
	password = db.Column(db.String, nullable=False)
	creation_date = db.Column(db.Date)							#make sure that Date is valid and DateTime isn't necessary
	updated_date = db.Column(db.Date)
	lost_password_key = db.Column(db.String, nullable=True)	#cryptography here, sha-512
	events = db.relationship('Event', backref='poster', lazy='dynamic') #look up in docs
	comments = db.relationship('Comment', backref='commenter', lazy='dynamic')
	articles = db.relationship('Article', backref='articler', lazy='dynamic')
	#ip_address 
	#google analytics should get us the rest of the metadata
	#any other metadata?

	def __init__(self, username=None, email=None, password=None, creation_date=None, updated_date=None, lost_password_key=None):
		self.username = username
		self.email = email
		self.password = password
		self.creation_date = datetime.datetime.utcnow()
		self.updated_date = datetime.datetime.utcnow()
		self.lost_password_key = lost_password_key

	def __repr__(self):
		return '<User %r>' % (self.username)


class Comment(db.Model):

	__tablename__ = "comments"

	comment_id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
	comment = db.Column(db.Text, nullable=False)
	event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'))
	comment_date = db.Column(db.Date)
	comment_update = db.Column(db.Date)
	article_id = db.Column(db.Integer, db.ForeignKey('articles.article_id'))

	def __init__(self, comment=None, comment_date=None, comment_update=None):
		self.comment = comment
		self.comment_date = datetime.datetime.utcnow()
		self.comment_update = datetime.datetime.utcnow()

	def __repr__(self):
		return '<Comment %r>' % (self.comment)

class Event(db.Model):

	__tablename__ = "events"

	event_id = db.Column(db.Integer, primary_key=True)
	event_title = db.Column(db.String, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
	event_date = db.Column(db.Date)
	event_update = db.Column(db.Date)	
	articles = db.relationship('Article', backref='the_source', lazy='dynamic')

	def __init__(self, event_title=None, event_date=None, event_update=None):
		self.event_title = event_title
		self.event_date = event_date
		self.event_update = event_update

	def __repr__(self):
		return '<Event %r>' % (self.event_title)

class Article(db.Model):

	__tablename__ = "articles"

	article_id = db.Column(db.Integer, primary_key=True)
	article_title = db.Column(db.String, nullable=False)
	source_id = db.Column(db.Integer, db.ForeignKey('sources.source_id'))
	url = db.Column(db.String, nullable=False) #cleaning string
	cleaned_text = db.Column(db.Text, nullable=False) 
	word_freq_dict = db.Column(db.Text, nullable=False) #IMPORTANTE COME BACK!!!  PICKLE TYPE?
	event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'))
	user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))


	def __init__(self, article_title=None, url=None, cleaned_text=None, word_freq_dict=None):
		self.article_title = article_title
		self.url = url
		self.cleaned_text = cleaned_text
		self.word_freq_dict = word_freq_dict

	def __repr__(self):
		return '<Article %r>' % (self.article_title)

class Source(db.Model):	#probly a lot of articles from different sources

	__tablename__ = "sources"

	source_id = db.Column(db.Integer, primary_key=True)
	source_name = db.Column(db.String, nullable=False)
	source_base_url = db.Column(db.String, nullable=False) #parseurl for this
	articles = db.relationship('Article', backref='source', lazy='dynamic')

	def __init__(self, source_name=None, source_base_url=None):
		source_name = self.source_name
		source_base_url = self.source_base_url

	def __repr__(self):
		return '<Source %r>' % (self.source_name)



