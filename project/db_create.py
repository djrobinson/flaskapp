from views import db
from models import Task
from datetime import date

db.create_all()
# db.session.add(Task("Finish this tutorial", date(2017, 9, 22), 10, 1))
# db.session.add(Task("Finish another tutorial", date(2017, 9, 29), 10, 1))

db.session.commit()