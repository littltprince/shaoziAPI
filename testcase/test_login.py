#encoding:utf-8
import unittest
import unittest
from  method.HttpResquest import HttpResquest
from method.operationpyxl import *
test_data=operationpyxl(data_path,'sheet1').get_data()
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.url='https://api.shaoziketang.com/wap/v2.8/login/data'
        self.data={"mobile":"15312362160","rand":"678123"}

    def test_right_login(self):
        res=HttpResquest().http_request(self.url,self.data,'post')
        print(res.json())
        try:
            self.assertEqual(200,res.json()['code'])
        except AssertionError as e:
            raise e
    def test_wrongphone_login(self):
        data={"mobile":"1531236216","rand":"678123"}
        res=HttpResquest().http_request(self.url,data,'post')
        print(res.json())
        try:
            self.assertEqual(200,res.json()['code'])
            print(res.status_code)
        except AssertionError as e:
            raise e
    def test_wrongpwd_login(self):
        data={"mobile":"15312362160","rand":"678124"}
        res=HttpResquest().http_request(self.url,data,'post')
        print(res.json())
        try:
            self.assertEqual(200,res.json()['code'])
        except AssertionError as e:
            raise e