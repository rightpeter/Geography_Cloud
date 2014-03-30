#!/usr/bin/env python
#encoding=utf-8

from db import *
import tornado.database
import sys


def installBuildingsTable():
    GCDatabase.reconnect()
    GCDatabase.execute("""CREATE TABLE `buildings`(
            id INT NOT NULL AUTO_INCREMENT, 
            name VARCHAR(30), 
            storey TINYINT,
            lng DOUBLE,
            lat DOUBLE,
            description TEXT,
            posttime TIMESTAMP, 
            PRIMARY KEY(id)) 
            DEFAULT CHARSET=utf8
    """)

def installRelationTable():
    GCDatabase.reconnect()
    GCDatabase.execute("""CREATE TABLE `relation`(
            id INT NOT NULL AUTO_INCREMENT, 
            fid INT,
            cid INT,
            storey TINYINT,
            posttime TIMESTAMP, 
            PRIMARY KEY(id)) 
            DEFAULT CHARSET=utf8
    """)

    
if __name__ == "__main__":
    print sys.argv
    if '-B' in sys.argv:
        installBuildingsTable()

    if '-R' in sys.argv:
        installRelationTable()

