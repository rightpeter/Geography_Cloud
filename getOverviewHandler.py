#!/usr/bin/python
#encoding: utf-8

import tornado.web
import tornado.ioloop
import os.path
import pickle
import json

from db import *
from myTools import *

#获取详细
class GetOverviewHandler(tornado.web.RequestHandler):
    def get(self, bid):
        overview = GCDatabase.query("""SELECT id, name, lng, lat FROM buildings WHERE id=%s""", bid)
        overview = overview[0]

        print overview 
        encodedjson = json.dumps(overview)
        self.write(encodedjson)
