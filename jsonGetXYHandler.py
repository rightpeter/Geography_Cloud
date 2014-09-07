#!/usr/bin/python
#encoding: utf-8

import tornado.web
import tornado.ioloop
import os.path
import pickle
import json

from myTools import *


#附近建筑物
class JsonGetXYHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "application/json")
        print self.request.uri
        try:
            lng = float(self.get_argument('lng'))
            lat = float(self.get_argument('lat'))
            dis = float(self.get_argument('ran'))
            callback = self.get_argument('callback')

            buildings_list = getNearby((lat, lng), dis) 
            encodedjson = json.dumps(buildings_list)
            self.write(callback+'('+encodedjson+')')
        except:
            self.write('error')

