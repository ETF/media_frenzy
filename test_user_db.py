#224 of 439
import os
import unittest

from mf_app import app, db
from mf_app.models import User
from config import basedir

TEST_DB = 'thetest.db'

class AddUser(unittest.TestCase):

	def setUp(self):
		app.config['TESTING'] = True
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, TEST_DB)
		self.app = app.test_client()
		db.create_all()

	#def tearDown(self):
		#db.drop_all()

'''	def test_user_setup(self):
		#def __init__(self, username=None, email=None, password=None, creation_date=None, updated_date=None, lost_password_key=None):
		new_user = User('validlength','valid@valid.com', 'validpasslength', 'lost_password_key')
		new_user2 = User('validlength2','valid@valid.com2', 'validpasslength2', 'lost_password_key2')
		db.session.add(new_user, new_user2)
		db.session.commit()
		test = db.session.query(User).all() 
		assert 'validlength' in test

if __name__ == '__main__':
	unittest.main()'''
