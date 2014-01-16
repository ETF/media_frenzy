from flask import Flask 
from flask.ext.sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from mf_app import views, models

#logging section
if not app.debug:
	import os
	import logging
	from logging import Formatter, FileHandler
	from config import basedir

	file_handler = FileHandler(os.path.join(basedir,'error.log')) #consecutive single quotes below are interesting
	file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s ' '[in %(pathname)s:%(lineno)d]'))
	#	   Setting Levels in Flask, I believe
	#	1.DEBUG 2.INFO 3.WARNING 4.ERROR 5.CRITICAL
	app.logger.setLevel(logging.INFO)
	file_handler.setLevel(logging.INFO)
	app.logger.addHandler(file_handler)
	app.logger.info('errors')