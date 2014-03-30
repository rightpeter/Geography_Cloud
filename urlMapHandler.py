#!/usr/bin/python
#encoding: utf-8

import tornado.web
import tornado.ioloop
import os.path
import pickle
import json

from myTools import *

class UrlMapHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("urlmap.html")
