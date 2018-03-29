# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/3/11 下午5:01
from utils.ParseExcel import ParseExcel
from utils import Log
from utils.HttpClient import *
from config.GloableData import *
from action.DataStore import RelyDataStore
from action.CheckResult import CheckResult
from action.WriteResult import WriteResult
from utils.EncryptUtil import EncryptMD5
from action.GetRely import GetRely
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def main():
    parE = ParseExcel()
    parE.loadWorkBook(interfaceFilePath)
    # 通过sheet名称获取sheet的实例对象
    sheetObj = parE.getSheetByName('API')
    # print sheetObj
    # 获取APIsheet表中的Activit列中的全部单元格对象，返回list
    activelist = parE.getColumn(sheetObj, Api_active)
    # print activelist
    for index, active_cell in enumerate(activelist[1:], 2):
        # print row
        row_value = active_cell.value
        if row_value.lower() == "y":
            # print row_value, index
            row = parE.getRow(sheetObj, index)

            APIName = row[Api_apiName - 1].value
            RequestUrl = row[Api_requestUrl - 1].value
            RequestMethod = row[Api_requestMethod - 1].value
            paramsType = row[Api_paramsType - 1].value
            ApiTestCase = row[Api_ApiTestCase - 1].value
            # print APIName, RequestUrl, paramsType, RequestMethod, ApiTestCase
            caseSheetObj = parE.getSheetByName(ApiTestCase)
            # print caseSheetObj.title
            case_active_list = parE.getColumn(caseSheetObj, Case_active)
            for case_index, case_row_active in enumerate(case_active_list[1:], 2):
                # row = parE.getRow(caseSheetObj, index)
                case_row_value = case_row_active.value
                if case_row_value.lower() == "y":
                    case_row = parE.getRow(caseSheetObj, case_index)
                    RequestData = case_row[Case_requestData - 1].value
                    ResponseCode = case_row[Case_responseCode - 1].value
                    ResponseData = case_row[Case_responseData - 1].value
                    DataStore = case_row[Case_dataStore - 1].value
                    CheckPoint = case_row[Case_checkPoint - 1].value
                    RelyData = case_row[Case_relyData - 1].value
                    # print RelyData
                    # print RequestData, ResponseCode, ResponseData, CheckPoint
                    # 获取接口case依赖的数据，并更新case里面的值
                    if RelyData and RequestData:
                        RequestData = "%s" % GetRely.get(eval(RequestData), eval(RelyData))
                    if APIName == u"用户登录":
                        print type(RequestData)
                        request_data = eval(RequestData)
                        request_data["password"] = EncryptMD5.encrypt_md5(request_data["password"])
                        RequestData = "%s" % request_data
                    httpC = HttpClient()
                    response = httpC.request(requestMethod=RequestMethod, requestUrl=RequestUrl,
                                             paramsType=paramsType, requestData=RequestData)
                    # 存储依赖数据
                    if response.status_code == 200 and DataStore:
                        storePoint = eval(DataStore)
                        dataS = RelyDataStore()
                        dataS.do(storePoint, eval(RequestData), response.json(), APIName, case_index - 1)
                        # print Request_data, Response_data
                    else:
                        if response.status_code != 200:
                            Log.info("接口响应失败")
                        else:
                            Log.info("不需要存储依赖数据")
                    if response.status_code == 200 and CheckPoint:
                        errorKey = CheckResult.check(response, eval(CheckPoint))
                        # 写入case执行结果
                        WriteResult.write(parE, caseSheetObj, response.text, errorKey, case_index)

                else:
                    Log.info("接口【%s】的第%s被忽略执行了" % (APIName, index - 1))
        # else:
        #     print "接口【%s】被忽略执行" % APIName


if __name__ == "__main__":
    main()
