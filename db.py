#!/usr/bin/env python
#encoding=utf-8
'''db'''
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import tornado.database

# GCDatabase = tornado.database.Connection(
#     "127.0.0.1:3306",
#     "geo_clo",
#     "geo_clo",
#     "geography_cloud",
# )

GCDatabase = tornado.database.Connection(
    "127.0.0.1:3306",
    "geo_clo",
    "geo_clo",
    "cippusrightpeter",
)
