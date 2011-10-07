#!/usr/bin/env python

import os
import time
import calendar
import datetime
import re
import Cookie
import email.utils
import operator
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from update import UpdateAppHandler
from control import ControlAppHandler

class MobileAppHandler(webapp.RequestHandler):
    def get(self, id):
		template_values = {'session_id': id}
		path = os.path.join(os.path.dirname(__file__), 'templates')
		path = os.path.join(path, 'mobile.html')
		self.response.out.write(template.render(path, template_values))