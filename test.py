#!/usr/bin pypthon
#coding: utf-8

import tornado.database

from db import *
from math import *
from myTools import *

# NewsDatabase.reconnect()
# 
# 
# NewsDatabase.execute("""CREATE TABLE `commTable`(
#             cid INT NOT NULL AUTO_INCREMENT, 
#             id int, 
#             level int, 
#             tolevel int, 
#             content text, 
#             posttime TIMESTAMP, 
#             PRIMARY KEY(cid)) 
#     """)
# 

# latA = float(raw_input('Input latA: '))
# lngA = float(raw_input('Input lngA: '))
# latB = float(raw_input('Input latB: '))
# lngB = float(raw_input('Input lngB: '))
# 
# latA = 90 - latA
# latB = 90 - latB
# 
# C = sin(latA)*sin(latB)*cos(lngA-lngB)
# 
# R = 6371.004
# Dis = R*acos(C)*pi/180
# 
# print Dis

pos = (34.591372, 119.2012912) 
print getNearby(pos, 279)
