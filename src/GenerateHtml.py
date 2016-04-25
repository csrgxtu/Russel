#!/usr/bin/env python
# coding=utf8
# Author: Archer Reilly
# File: GenerateHtml.py
# Desc: Generate a html file from results from Baidu OCR
# Date: 25/Apr/2016
#
# Produced By BR
from Utility import loadSeasons

lines = loadSeasons('./dest.csv')

for line in lines:
    print '<img src="http://192.168.100.2:8082/imgs/' + line.split(',')[0] + '">' +  line.split(',')[1] + '</img><input type="checkbox" onclick="check(this)"><input type="checkbox" onclick="remove(this)"><br/>'
