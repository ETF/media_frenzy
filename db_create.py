from mf_app import db
from mf_app.models import User, Comment, Event, Article, Source


db.drop_all()
db.create_all()

#test input data
admin = User('admin', 'admin@admin.com', 'admin1', 'fakelostpass')
guest = User('guest', 'guest@guest.com', 'guest1', 'fakelostpass')

#User(name=None, email=None, password=None, creation_date=None, updated_date=None, lost_password_key=None

db.session.add(admin)
db.session.add(guest)

db.session.commit()

users = User.query.all()
print(users)