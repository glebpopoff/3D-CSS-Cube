import logging
from google.appengine.ext import db

class RemoteModel(db.Model):
	rec_date = db.DateTimeProperty(auto_now_add=True)
	rec_id = db.StringProperty()
	rec_direction = db.StringProperty()