from mf_app import app, db
from mf_app.models import User
from flask import Flask, render_template, request, session, flash, redirect, url_for


@app.route('/')
def directory():
	return render_template('directory.html')

@app.route('/main')
def main():
	return render_template('main.html')