#encoding:utf-8
import unittest
from testcase.test_login import TestLogin
import time
from method import htmltestrunner
import os
from method.operationpyxl import *
test_data=operationpyxl(data_path,'sheet1').get_data()

#通过创建实例的方式来加载用例,注意Excel中每个参数的数据类型，除了数字其他基本全是‘str'格式
suite=unittest.TestSuite()
for item in test_data:
    # print(type(item['url']),type(item['data']),type(item['method']),type(item['expect']))
    # print(item['url'],item['data'],item['method'],item['expect'])
    suite.addTest(TestLogin('test_login',item['url'],eval(item['data']),item['method'],item['expect']))
with open('report.html','wb') as file:
    runner=htmltestrunner.HTMLTestRunner(file,verbosity=2,title='测试的标题',description='勺子课堂API')
    runner.run(suite)
# a=os.getcwd()
# now=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#1、通过loader的方式来加载用例
# filename='result_report.html'
# suite=unittest.TestLoader().discover(start_dir='testcase',pattern='test*.py',top_level_dir= None)
# with open(filename,'wb') as file:
#     runner=htmltestrunner.HTMLTestRunner(file,
#                                          verbosity=2,
#                                          title='测试报告',
#                                          description='勺子课堂api'
#                                          )
#     runner.run(suite)