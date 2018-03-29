# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/3/18 下午4:25

from config.GloableData import Request_data, Response_data
from utils import Log


class RelyDataStore(object):
    def __init__(self):
        pass

    def do(self, storePoint, requestSource, responseSource, apiName, caseIndex):
        # 存储依赖数据存在两种情况
        # 1. 存储请求参数里面的依赖数据
        # 2. 存储响应body中的依赖数据
        if "request" in storePoint:
            for i in storePoint["request"]:
                if i in requestSource:
                    if apiName in Request_data:
                        if caseIndex in Request_data[apiName]:
                            Request_data[apiName][caseIndex][i] = requestSource[i]
                        else:
                            Request_data[apiName][caseIndex] = {i: requestSource[i]}
                    else:
                        Request_data[apiName] = {caseIndex: {i: requestSource[i]}}
                else:
                    Log.info("需要存储的key【%s】不存在" % i)
        elif "response" in storePoint:
            for i in storePoint["response"]:
                if i in responseSource:
                    if apiName in Response_data:
                        if caseIndex in Response_data[apiName]:
                            Response_data[apiName][caseIndex][i] = responseSource[i]
                        else:
                            Response_data[apiName][caseIndex] = {i: responseSource[i]}
                    else:
                        Response_data[apiName] = {caseIndex: {i: responseSource[i]}}
                else:
                    Log.info("需要存储的key【%s】不存在" % i)
