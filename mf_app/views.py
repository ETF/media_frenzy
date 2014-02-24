from mf_app import app, db
from mf_app.models import User, Article
from mf_app.forms import RegisterForm, LoginForm, StartFrenzy
from api import counts_pages_words, textify
from flask import render_template, request, session, flash, redirect, url_for, jsonify
from functools import wraps
from sqlalchemy.exc import IntegrityError
import json

#ERROR AND LOGIN HANDLING
def flash_errors(form):
	for field, errors in form.errors.items():
		for error in errors:
			flash(u"Error in the %s field - %s" % (getattr(form, field).label.text, error), 'error')

def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash('You need to login first')
			return redirect(url_for('directory'))
	return wrap
#END ERROR AND LOGIN HANDLING


#ROUTES

#LOGIN FUNCTION ON DIRECTORY PAGE
@app.route('/', methods=['GET','POST'])
def index():
	error = None
	text1_wfreq = {'applause': 77, 'america': 33, 'security': 16, 'american': 15, 'afghanistan': 13, 'good': 13, 'new': 13, 'world': 13}
	text2_wfreq = {'applause': 103, 'more': 40, 'now': 37, 'can': 31, 'jobs': 24, 'new': 24, 'all': 23, "let's": 23}
	return render_template('directory.html', form=StartFrenzy(request.form), error=error, text1_wfreq=text1_wfreq, text2_wfreq=text2_wfreq)

@app.route('/login', methods=['POST'])
def login():
	error = None
	if request.method == 'POST':
		u = User.query.filter_by(username=request.form['username'], password=request.form['password']).first()
		if u is None:
			error = 'Invalid username or password'
		else:
			session['logged_in'] = True
			session['user_id'] = u.user_id
			flash('You are now logged in')
		return render_template('directory.html', form=LoginForm(request.form), error=error)
	return render_template('directory.html', form=LoginForm(request.form), error=error)

@app.route('/start_frenzy', methods=['POST'])
def start_frenzy():
	error = None

	#mock data
	#text1_wfreq = {'applause': 77, 'america': 33, 'security': 16, 'american': 15, 'afghanistan': 13, 'good': 13, 'new': 13, 'world': 13}
	#text2_wfreq = {'applause': 103, 'more': 40, 'now': 37, 'can': 31, 'jobs': 24, 'new': 24, 'all': 23, "let's": 23}
	
	form = StartFrenzy(request.form)
	# Test the type of request.form
	# may require type conversion
	if form:
		#this = type(form.url)
		#this = this.__html__
		#this = type(this)
		#flash(form.url.data)
		#import pdb; pdb.set_trace()
		w_url = str(form.url.data)
		
		#w_url = w_url.__html__
		
		#the_title = results["title"]()

		#json_top_ten1 = 
		reading_text = textify(w_url)
	else:
		flash('Not working')	

	if request.method == 'POST':   #does the request happen before WTForms catches it or not
		return render_template('main.html', top_tenJSON=get_global_JSON(w_url), reading_text=reading_text, form=form, error=error)
	else:
		return render_template('directory.html', error=error)

def get_global_JSON(url, context=None):
	results = counts_pages_words(url)
	top_ten1 = results["freq_dist"][0:10] #still type list of tuple pairs
	return json.dumps(top_ten1)

@app.route('/get_JSON_comments')
def get_JSON_comments():
	# fake_comments = ["squirrels are crazy", "ya, you should see them on a house boat", "they're smarter than you think", "Right!? They are highly intelligent", "And crazy... For nuts", "My dog likes nuts", "Word", "Did you hear about my grandma?", "Was it your grandma that got bit by the dog", "Ya, on the crazy house boat"]
	comment_frequency = [
	  ["boats", 55],
	  ["slum", 19],
	  ["squirrels", 14],
	  ["wordup", 9],	  
	  ["seepage", 5],
	  ["grandma", 4],
	  ["Gilligan", 2],
	  ["pirate", 1]]
	return jsonify(results=comment_frequency)

#REGISTER FUNCTION ONLY NEEDED ONCE
@app.route('/register', methods=['GET', 'POST'])
def register():
	error = None
	form = RegisterForm(request.form, csrf_enabled=False)
	if form.validate_on_submit():
		new_user = User(form.username.data,
						form.email.data,
						form.password.data,
						'lost_pass_key',
						)
		try: 
			db.session.add(new_user)
			db.session.commit()
			flash('Thank you for registering. Please Login')
		#PRECISION NEEDS TO BE IMPROVED UPON
		except IntegrityError:
			error = 'That username and/or email already exists. Please try again.'
		return redirect(url_for('login'))
	else:
		flash_errors(form)
	return render_template('register.html', form=form, error=error)


@app.route('/main')
@login_required
def main():
	#text1_list = [77,33,16,15,13,13,13,13]
	text1_wfreq = {'applause': 77, 'america': 33, 'security': 16, 'american': 15, 'afghanistan': 13, 'good': 13, 'new': 13, 'world': 13}
	text2_wfreq = {'applause': 103, 'more': 40, 'now': 37, 'can': 31, 'jobs': 24, 'new': 24, 'all': 23, "let's": 23}
	#easywords1 = [key for key in text1_wfreq.keys()]
	#easywords2 = [key for key in text2_wfreq.keys()]
	#easyfreq1 = [value for value in text1_wfreq.values()]
	#easyfreq2 = [value for value in text2_wfreq.values()]
	error = None
	#
	#easywords1=easywords1, easywords2=easywords2, easyfreq1=easyfreq1, easyfreq2=easyfreq2
	return render_template('main.html', form=LoginForm(request.form), error=error, text1_wfreq=text1_wfreq, text2_wfreq=text2_wfreq)

