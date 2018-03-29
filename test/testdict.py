# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/3/25 下午5:33


ss = {u'\u7528\u6237\u6ce8\u518c': {1: {'username': 'wcx', 'password': 'wcx123wac'}, 2: {'username': 'zxc', 'password': 'zxc123zxc'}}}
# print type(ss)
keyS = '[u"用户注册"][1][u"username"]'
print ss[u"用户注册"][1][u"username"]
print eval("%s%s" %ss %keyS)