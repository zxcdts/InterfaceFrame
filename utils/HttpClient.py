# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/3/18 下午2:02
import requests
import json


class HttpClient(object):
    def __init__(self):
        pass

    def request(self, requestMethod, requestUrl, paramsType, requestData=None, headers=None, cookies=None, **kwargs):
        # print requestMethod, requestUrl, paramsType, requestData
        if requestMethod.lower() == "post":
            if paramsType.lower() == "form":
                response = self.__post(url=requestUrl, data=json.dumps(eval(requestData)),
                                       headers=headers, cookies=cookies)
            elif paramsType.lower() == "json":
                response = self.__post(url=requestUrl, json=requestData, headers=headers, cookies=cookies)
        elif requestMethod.lower() == "get":
            if paramsType.lower() == "url":
                url = "%s%s" % (requestUrl, requestData)
                response = self.__get(url=url, headers=headers, cookies=cookies)
            elif paramsType.lower() == "params":
                response = self.__get(url=requestUrl, params=requestData, headers=headers, cookies=cookies)
        return response

    def __post(self, url, data=None, json=None, **kwargs):
        response = requests.post(url=url, data=data, json=json)
        return response

    def __get(self, url, params=None, **kwargs):
        response = requests.get(url=url, params=params)
        return response
