#!/usr/bin/env python
# coding=utf-8
# Author: Archer Reilly
# File: BaiduOCR.py
# Desc: use Baidu OCR Services processing the images
# Date: 21/Apr/2016
#
# Produced By BR
import sys, urllib, urllib2, json
import base64
import ast
from bs4 import BeautifulSoup
import time
from Utility import loadSeasons, appendstr2fileutf8

url = 'http://apis.baidu.com/idl_baidu/baiduocrpay/idlocrpaid'
data = {}
data['fromdevice'] = "pc"
data['clientip'] = "192.168.100.3"
data['detecttype'] = "LocateRecognize"
data['languagetype'] = "CHN_ENG"
data['imagetype'] = "1"

# first, open names.txt
# for each name, build a csv row and store it
names = loadSeasons('./names.txt')
for name in names:
    time.sleep(2)
    file_object = open('/bookdata/liqiang/Downloads/books/' + name, 'rb')
    try:
         tmp = file_object.read( )
    finally:
         file_object.close( )
    data['image'] = base64.b64encode(tmp)

    decoded_data = urllib.urlencode(data)
    req = urllib2.Request(url, data = decoded_data)

    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    req.add_header("apikey", "150281dc441994b2d21ddb0e57a9bd48")

    resp = urllib2.urlopen(req)
    content = resp.read()
    if(content):
        if bool(BeautifulSoup(content, "html.parser").find()):
            print content
            print "Got Html, Not Right"
            time.sleep(30)
            continue
            # break

        print content
        if len(ast.literal_eval(content)['retData']) == 0:
            res = name + ',' + ''
            appendstr2fileutf8(res, './result.csv')
            # continue
        else:
            title = ast.literal_eval(content)['retData'][0]['word']
            print title
            res = name + ',' + title
            appendstr2fileutf8(res, './result.csv')
