from mf_app import app, db
from mf_app.models import User
from mf_app.forms import RegisterForm, LoginForm
from flask import Flask, render_template, request, session, flash, redirect, url_for
from functools import wraps
from sqlalchemy.exc import IntegrityError

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
@app.route('/', methods=['GET', 'POST'])
def directory():
	error = None

	#REGISTER FUNCTION
	form = RegisterForm(request.form, csrf_enabled=False)
	if form.validate_on_submit():
		new_user = User(form.name.data,
						form.email.data,
						form.password.data,
						)
		try: 
			db.session.add(new_user)
			db.session.commit()
			flash('Thank you for registering. Please Login')
		#PRECISION NEEDS TO BE IMPROVED UPON
		except IntegrityError:
			error = 'That username and/or email already exists. Please try again.'
	else:
		flash_errors(form)

	#LOGIN FUNCTION
	if request.method == 'POST':
		u = User.query.filter_by(name=request.form['name'],
								 password=request.form['password']).first()
		if u is None:
			error = 'Invalid username or password'
		else:
			session['logged_in'] = True
			session['user_id'] = u.user_id
			flash('You are now logged in')
		#JUST FOR TESTING THIS SHOULD BE CHANGED LATER
		return render_template('directory.html', form=form, error=error)
	return render_template('directory.html', form=form, error=error)

@app.route('/main')
def main():
	return render_template('main.html')