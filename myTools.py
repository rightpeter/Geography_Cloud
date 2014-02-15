#!/usr/bin/python
#encoding: utf-8

import tornado.web
import tornado.ioloop
import os.path
import pickle
import json

from datetime import *

from db import *
from math import *

def disAB(pos1, pos2):
    pos1[0] = 90 - pos1[0]
    pos2[0] = 90 - pos2[0]

    C = sin(pos1[0])*sin(pos2[0])*cos(pos1[1]-pos2[1])

    R = 6371.004
    Dis = R*acos(C)*pi/180

    return Dis 

def getNearby(pos, dis):
    GCDatabase.reconnect()

    buildings_dic = GCDatabase.query("""SELECT id FROM buildings WHERE
    6371.004*ACOS(SIN(%s)*SIN(lat)*COS(%s-lng)+COS(%s)*COS(lat))*PI()/180 <
    %s""", pos[0], pos[1], pos[0], dis)

    buildings = []
    for k in buildings_dic:
        buildings.append(int(k['id']))

    return buildings

class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

def matchBuildings(pic, buildings_list):
    return buildings_list[0]
