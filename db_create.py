from mf_app import db
from mf_app.models import User, Comment, Event, Article, Source


db.drop_all()
db.create_all() #is this necessary to insert mock data?

#TEST USER DATA
#def __init__(self, username=None, email=None, password=None, creation_date=None, updated_date=None, lost_password_key=None):
#dates set to datetime.datetime.utcnow()
admin = User('admin', 'admin@admin.com', 'admin1', 'fakelostpasskey1')
guest = User('guest', 'guest@guest.com', 'guest1', 'fakelostpasskey1')

#TEST COMMENT DATA
comment1 = Comment("this is not a substantive comment")

#TEST EVENT DATA
#event1 = Event('NYTimes', 'www.nytimes.com', '1')
event1 = Event('SF Housing', 2)

#TEST ARTICLE DATA
#def __init__(self, article_title=None, url=None, cleaned_text=None, word_freq_dict=None)
article1 = Article("Dog eats Grandmother", "www.realnews.com", "cleaned text, this could get really long and punc could matter in the db", "word freq dictionary I guess")

#TEST SOURCE DATA
#def __init__(self, source_name=None, source_base_url=None):
source1 = Source('NYTimes', 'www.nytimes.com')


#User(name=None, email=None, password=None, creation_date=None, updated_date=None, lost_password_key=None

#INSERT MOCK DATA
db.session.add(admin)
db.session.add(guest)
db.session.add(event1)
db.session.add(comment1)
db.session.add(article1)
db.session.add(source1)

db.session.commit()

users = User.query.all()
print(users)