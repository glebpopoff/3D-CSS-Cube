#!/usr/bin/env python
# Retrieves cube viewport direction (up,down,left,right) based on id
#

import os
import re
import logging
from UserString import MutableString
from django.utils import simplejson
from google.appengine.ext import webapp 
from google.appengine.ext import db
from google.appengine.ext.webapp import util
import datahandler

class UpdateAppHandler(webapp.RequestHandler):
	def get(self,id):
		self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
		#output to the browser
		obj = datahandler.getData(id)
		if (obj and len(obj) > 0):
			direction = obj[0].rec_direction
			#delete this record
			obj[0].delete()
			self.response.out.write('{"viewport_dir": "%s"}' % direction)
		else:
			self.response.out.write('{"status": "unable to get data by id"}')