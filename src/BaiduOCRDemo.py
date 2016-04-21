#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json
import base64
import ast
from Utility import appendstr2fileutf8, appendstr2file

url = 'http://apis.baidu.com/idl_baidu/baiduocrpay/idlocrpaid'

data = {}
data['fromdevice'] = "pc"
# data['clientip'] = "10.10.10.0"
data['clientip'] = "192.168.100.2"
data['detecttype'] = "LocateRecognize"
data['languagetype'] = "CHN_ENG"
data['imagetype'] = "1"

file_object = open('../data/ffebb7f8-0a6c-4380-b4b8-ee8b4b8ae7a2.jpg_5.jpg','rb')
try:
     tmp = file_object.read( )
finally:
     file_object.close( )
data['image'] = base64.b64encode(tmp)


decoded_data = urllib.urlencode(data)
req = urllib2.Request(url, data = decoded_data)

req.add_header("Content-Type", "application/x-www-form-urlencoded")
req.add_header("apikey", "1466dccc8ec8e42feaf18f2e05c543fc")

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    # print(content)
    title = ast.literal_eval(content)['retData'][0]['word']
    print title
    # print type(title), type(unicode(title, 'utf-8'))
    # print unicode(title, 'utf-8').encode('utf-8', 'ignore')
    # print u'\u4e2d\u56fd\u4eba\u7684\u670d\u9970\u548c\u4e60\u4fd7\u56fe\u9274'
    # appendstr2fileutf8(u'\u4e2d\u56fd\u4eba\u7684\u670d\u9970\u548c\u4e60\u4fd7\u56fe\u9274', './result.csv')
    appendstr2fileutf8(title, './result.csv')
