#!/usr/bin/python
#encoding: utf-8

import tornado.web
import tornado.ioloop
import os.path
import pickle
import json

from myTools import *

#附近建筑物
class GetXYHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("position.html")

    def post(self):
        self.set_header("Content-Type", "application/json")
        userPosition = (float(self.get_argument("X")),
                float(self.get_argument("Y")))
        place_list = []
        for dirs in os.listdir(r'./static/buildings'):
            print dirs
            building_path = './static/buildings/' + dirs + '/info.pickle'
            try:
                with open(building_path, 'rb') as tmp:
                    building_dict = pickle.load(tmp)
                tmpId = building_dict['id']
                tmpPosition = building_dict['position']
                if near(userPosition, tmpPosition):
                    place_list.append({"id":tmpId, 'position':tmpPosition,})
	    except:
                print "file error"
        encodedjson = json.dumps(place_list)
        self.write(encodedjson)

