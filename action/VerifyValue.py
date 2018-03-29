# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/3/25 下午2:03
import re


class VerifyValue(object):
    def __init__(self):
        pass

    @classmethod
    def verify(cls, sourValue, realValue):
        flag = False
        if isinstance(sourValue, dict):
            # 说明需要通过正则匹配
            regStr = sourValue["value"]
            try:
                re.match(r"%s" % regStr, r"%s" % realValue).group()
            except AttributeError, e:
                flag = False
            else:
                flag = True
        else:
            if sourValue == realValue:
                flag = True
        return flag


if __name__ == "__main__":
    sourValue = {"value": "\w+"}
    print VerifyValue.verify(sourValue, "12sdfe")
    print VerifyValue.verify("12sddfe", "12sdfe")
