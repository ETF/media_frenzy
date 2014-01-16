from mf_app import db
from mf_app.models import User

db.create_all()

#test input data
admin = User('admin', 'admin@admin.com', 'admin')
guest = User('guest', 'guest@guest.com', 'guest')

db.session.add(admin)
db.session.add(guest)

db.session.commit()

users = User.query.all()
print(users)