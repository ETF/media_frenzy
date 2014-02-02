#224 of 439
import os
import unittest

from app import app, db
from app.models import User
from config import basedir

TEST_DB = 'thetest.db'

class AddUser(unittest.TestCase):

	def setUp(self):
		app.config['TESTING'] = True
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, TEST_DB)
		self.app = app.test_client()
		db.create_all()

	def tearDown(self):
		db.drop_all()

	def test_user_setup(self):
		new_user = User('validlength','valid@valid.com', 'validpasslength')
		db.session.add(new_user)
		db.session.commit()

if __name__ == '__main__':
	unittest.main()
