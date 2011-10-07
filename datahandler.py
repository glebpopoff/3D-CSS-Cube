import datetime
import time
from google.appengine.ext import db
from models import RemoteModel

#retrieves data by ID
def getData(recordId):
	q = RemoteModel.all()
	q.filter("rec_id =", recordId)
	results = q.fetch(1)
	return results

#stores data	
def putData(recordId, direction):
	d = RemoteModel(key_name='%s_%s' % (recordId,direction))
	d.rec_id = recordId
	d.rec_direction = direction
	d.put()