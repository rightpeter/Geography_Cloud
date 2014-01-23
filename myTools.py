#!/usr/bin/python
#encoding: utf-8

import tornado.web
import tornado.ioloop
import os.path
import pickle
import json

def near(position1, position2):
    return 1
    # if ( (position1[0]-position2[0])**2 + (position1[1]-position2[1])**2 <=
    #         10000):
    #     return 1
    # else:
    #     return 0 

