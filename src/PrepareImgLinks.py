#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# File: PrepareImgLinks.py
# Desc: get image links from scan collection
# Date: 12/Apr/2016
#
# Produced By BR
from pymongo import MongoClient
from Utility import appendstr2file

url = 'mongodb://linyy:rioreader@192.168.200.20/bookshelf'
client = MongoClient(url)

db = client['bookshelf']
c = db['scan']

for doc in c.find():
    print doc[u'image']
    appendstr2file(doc[u'image'], '../data/links.csv')
