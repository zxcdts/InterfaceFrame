# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/3/11 下午3:02
import requests
import json

print "register------"
data = json.dumps({'username': 'lily', 'password': 'wcx123wac', 'email': 'lily@qq.com'})#
r = requests.post('http://39.106.41.11:8080/register/', data=data)
print r.status_code
print r.text
print type(r.json())
print str(r.json())
