import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'just_test.db'

SECRET_KEY = '9VCxvsnlUcMe'

DATABASE_PATH = os.path.join(basedir, DATABASE)

SQLALCHEMY_DATABASE_URI = 'sqlite:////' + DATABASE