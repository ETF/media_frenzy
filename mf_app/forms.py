#using WTF-0.9.3
from flask_wtf import Form
from wtforms import TextField, DateField, IntegerField, SelectField, PasswordField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegisterForm(Form):
	##NOTE: ADEQUATE ERROR MESSAGES AND POSSIBLE PASSWORD STRENGTH BAR NEEDED HERE!!!
	name = TextField('Username', validators=[DataRequired(), Length(min=4, max=25)])
	email = TextField('Email', validators=[DataRequired(), Length(min=6, max=40)])
	password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match'), Length(min=6, max=40)])
	confirm = PasswordField('Repeat Password', validators=[DataRequired()])

class LoginForm(Form):
	name = TextField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])