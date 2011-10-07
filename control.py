#!/usr/bin/env python
# Saves cube viewport direction (up,down,left,right) based on id
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

class ControlAppHandler(webapp.RequestHandler):
	def get(self,id,dir):
		self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
		if (id and dir):
			#lets see if we already have record by the same ID
			obj = datahandler.getData(id)
			if (obj and len(obj) > 0):
				obj[0].delete()
			#store new direction
			datahandler.putData(id, dir)
			#output to the browser
			self.response.out.write('{"status": "stored successfully"}')
		else:
			self.response.out.write('{"status": "invalid id or direction"}')