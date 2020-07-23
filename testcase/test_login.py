#encoding:utf-8
import unittest
import unittest
from  method.HttpResquest import HttpResquest
from method.operationpyxl import *
from ddt import ddt,data,unpack
test_data=operationpyxl(data_path,'login').get_data()
# print("第一个test_data是",test_data)
@ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        print('开始测试啦')
    # def __init__(self,methodname,url,data,method,expect):
    #     super(TestLogin,self).__init__(methodname)
    #     self.url = url
    #     self.data = data
    #     self.method = method
    #     self.expect = expect

    @data(*test_data)
    def test_login(self,item):
        # print("第二次的打印：",test_data)
        # for item in test_data:
        print("第{0}条用例的简介为{1}，测试的参数为{2}".format(item['case_id'],item['title'],(item['url'],item['data'],item['method'])))
        res = HttpResquest().http_request(item['url'],eval(item['data']),item['method'])
        # print(self.url,self.data,self.method)
        print(type(res.json()['code']))
        print(res.json())
        operationpyxl(data_path,'login').write_fact(item['case_id']+1,res.json()['code'])
        try:
            self.assertEqual(item['expect'], res.json()['code'])
            operationpyxl(data_path, 'login').write_result(item['case_id'] + 1, 'pass')
        except AssertionError as e:
            print("test_login的错误是{}".format(e))
            operationpyxl(data_path, 'login').write_result(item['case_id'] + 1, 'Failed')
            raise e
        # finally:
        #     operationpyxl(data_path, 'login').write_result(item['case_id'] + 1, str(res.json()))














































































    # def test_right_login(self):
    #     res=HttpResquest().http_request(self.url,self.data,'post')
    #     print(res.json())
    #     try:
    #         self.assertEqual(200,res.json()['code'])
    #     except AssertionError as e:
    #         raise e
    # def test_wrongphone_login(self):
    #     data={"mobile":"1531236216","rand":"678123"}
    #     res=HttpResquest().http_request(self.url,data,'post')
    #     print(res.json())
    #     try:
    #         self.assertEqual(200,res.json()['code'])
    #         print(res.status_code)
    #     except AssertionError as e:
    #         raise e
    # def test_wrongpwd_login(self):
    #     data={"mobile":"15312362160","rand":"678124"}
    #     res=HttpResquest().http_request(self.url,data,'post')
    #     print(res.json())
    #     try:
    #         self.assertEqual(200,res.json()['code'])
    #     except AssertionError as e:
    #         raise e