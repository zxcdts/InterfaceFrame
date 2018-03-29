# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/3/18 下午3:32
import os
# 获取项目根目录
Project_path = os.path.dirname(os.path.dirname(__file__))
# 日志配置文件路径
Logger_conf_path = Project_path + u'/config/Logger.conf'
# 测试用例路径
interfaceFilePath = Project_path + u"/TestData/inter_test_data.xlsx"

# 接口信息
Api_apiName = 2
Api_requestUrl = 3
Api_requestMethod = 4
Api_paramsType = 5
Api_ApiTestCase = 6
Api_active = 7
# 测试用例
Case_requestData = 1
Case_relyData = 2
Case_responseCode = 3
Case_responseData = 4
Case_dataStore = 5
Case_checkPoint = 6
Case_active = 7
Case_status = 8
Case_errorInfo = 9
Case_execTime = 10

# 存储请求依赖数据
Request_data = {}
# 存储响应依赖参数
Response_data = {}
