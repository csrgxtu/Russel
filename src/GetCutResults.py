#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# Date: 18/Apr/2016
# File: GetCutResults.py
# Desc: get cut results of a image by accessing the api and store it
# in a csv file
#
# Produced By BR
import unirest
from Utility import loadSeasons, appendstr2file

INPUT = '../data/names.txt'
OUTPUT = '../data/results.csv'
# API = 'https://dev-riowechat.beautifulreading.com/cutbook/'
# API = 'http://localhost:8090/cutbook/'
API = 'http://192.168.100.2:8090/cutbook/'

names = loadSeasons(INPUT)
for name in names:
    url = API + name
    unirest.timeout(120)
    response = unirest.get(url)
    if response.code == 200:
        print response.body
        row = name + ',' + str(response.body[u'data'])
        appendstr2file(row, OUTPUT)
    else:
        row = name + ',' + str(0)
        appendstr2file(row, OUTPUT)
