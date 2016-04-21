#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# File: UnirestFileUpload.py
# Desc: upload a image file to the api
# Date: 16/Apr/2016
#
# Produced By BR
import unirest
import os

url = 'http://192.168.100.2:8090/cutbook'

files = os.listdir('../data/img')
for img in files:
  print img
  params = {
    "file": open('../data/img/' + img, mode='r')
  }
  response = unirest.put(url, params=params)
  print response
