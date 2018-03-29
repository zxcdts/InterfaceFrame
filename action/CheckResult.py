# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/3/25 上午11:24
from action.VerifyValue import VerifyValue
from GetKey import getKey


class CheckResult(object):
    def __init__(self):
        pass

    @classmethod
    def check(cls, response, checkPoint):
        responseBody = response.json()
        errorKey = {}
        for key, value in checkPoint.items():
            keyS = getKey(key)
            realityV = eval("responseBody" + keyS)
            # print realityV
            # 接下来就是进行值的校验
            resFlag = VerifyValue.verify(value, realityV)
            if not resFlag:
                errorKey[key] = realityV
        return errorKey


if __name__ == "__main__":
    keyStr = "links->0->name"
    keyStr = "name"
    checkPoint = {"name": {"value": "\w+$"}, "age": {"value": "[0-9]+$"}, "links->0->name": "大众"}
    responseBody = {"name": "lily///", "age": "ss",
                    "links": [{"id": 1, "name": "大众"}, {"id": 33, "name": "奥迪"}, {"id": 63, "name": "日产"}]}
    # getKey(keyStr)
    errorKey = CheckResult.check(responseBody, checkPoint)
    print errorKey
