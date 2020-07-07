#encoding:utf-8
import unittest
import time
from method import htmltestrunner
import os
a=os.getcwd()
now=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
filename='result_report.html'

suite=unittest.TestLoader().discover(start_dir='testcase',pattern='test*.py',top_level_dir= None)
with open(filename,'wb') as file:
    runner=htmltestrunner.HTMLTestRunner(file,
                                         verbosity=2,
                                         title='测试报告',
                                         description='勺子课堂api'
                                         )
    runner.run(suite)