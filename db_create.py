from mf_app import db
from mf_app.models import User, Comment, Event, Article, Source


db.drop_all()
db.create_all()

#test input data
admin = User('admin', 'admin@admin.com', 'admin1', 'fakelostpass')
guest = User('guest', 'guest@guest.com', 'guest1', 'fakelostpass')

#event1 = Event('NYTimes', 'www.nytimes.com', '1')
event1 = Event('SF Housing', 2)

#def __init__(self, source_name=None, source_base_url=None):
source1 = Source('NYTimes', 'www.nytimes.com')


#User(name=None, email=None, password=None, creation_date=None, updated_date=None, lost_password_key=None

db.session.add(admin)
db.session.add(guest)
db.session.add(event1)
db.session.add(source1)

db.session.commit()

users = User.query.all()
print(users)