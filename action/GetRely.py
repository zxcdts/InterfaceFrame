# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/3/25 下午4:39
from GetKey import getKey
from config.GloableData import Request_data, Response_data


# Request_Data = {"用户注册": {"1": {"username": "wcx", "password": "12321"}}}
# Response_Data = {"用户注册": {"1": {"username": "wcx", "password": "wewewew"}}}


class GetRely(object):
    def __init__(self):
        pass

    @classmethod
    def get(cls, requestData, relyData):
        if relyData.has_key("request"):
            for key, value in relyData["request"].items():
                # print Request_data
                keyS = getKey(value)
                # print keyS
                try:
                    keyExp = u"Request_data" + '%s' % keyS
                    print isinstance(keyExp, unicode)
                    value = eval(keyExp)
                    # value = eval(u"Request_data" + u"%s" % keyS)
                except KeyError, e:
                    print e
                    print "Request_Data字典中不存在依赖数据key：%s" % keyS

                else:
                    requestData[key] = value
        if relyData.has_key("response"):
            for key, value in relyData["response"].items():
                keyS = getKey(value)
                try:
                    keyExp = u"Response_data" + '%s' % keyS
                    print isinstance(keyExp, unicode)
                    value = eval(keyExp)
                except KeyError, e:
                    print "Response_Data字典中不存在依赖数据key：%s" % keyS
                else:
                    requestData[key] = value
        return requestData


if __name__ == "__main__":
    print Request_data, Response_data
    requestData = {"username": "", "password": ""}
    # relyData = {"request": {"username": "用户注册->1->username", "password": "用户注册->1->password"}}
    # relyData = {"response": {"username": "用户注册->1->username", "password": "用户注册->1->password"}}
    relyData = {"request": {"username": "用户注册->1->username"}, "response": {"password": "用户注册->1->password"}}
    print GetRely.get(requestData, relyData)
