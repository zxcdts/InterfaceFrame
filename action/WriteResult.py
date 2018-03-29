# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/3/25 下午3:01
from config.GloableData import *
from utils.FormatTime import date_time_chinese


class WriteResult(object):
    def __init__(self):
        pass

    @classmethod
    def write(cls, wbObj, sheetObj, responseData, errorKey, rowNum):
        print responseData, errorKey
        try:
            # 写入返回值
            wbObj.writeCell(sheet=sheetObj, content=responseData, rowNo=rowNum, colsNo=Case_responseData)
            if errorKey:
                # 写入返回状态
                wbObj.writeCell(sheet=sheetObj, content="faile", rowNo=rowNum, colsNo=Case_status)
                # 写入错误信息
                wbObj.writeCell(sheet=sheetObj, content="%s" % errorKey, rowNo=rowNum, colsNo=Case_errorInfo)
            else:
                # 写入返回状态
                wbObj.writeCell(sheet=sheetObj, content="pass", rowNo=rowNum, colsNo=Case_status)
            # 写入执行时间
            wbObj.writeCell(sheet=sheetObj, content=date_time_chinese(), rowNo=rowNum, colsNo=Case_execTime)
        except Exception, e:
            print e


if __name__ == "__main__":
    print '111'
