# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/3/25 下午4:47


def getKey(keyStr):
    # ["links"][0]["name"]
    keyS = ""
    if keyStr and "->" in keyStr:
        keyTup = keyStr.split("->")
        for i in keyTup:
            if i.isdigit():
                keyS += '[%s]' % i
            else:
                keyS += '[u"%s"]' % i
    else:
        keyS += '["%s"]' % keyStr
    return keyS


def getRelyKey(keyStr):
    # ["links"][0]["name"]
    keyS = ""
    if keyStr and "->" in keyStr:
        keyTup = keyStr.split("->")
        for i in keyTup:
            keyS += '["%s"]' % i
    else:
        keyS += '["%s"]' % keyStr
    return keyS