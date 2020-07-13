import unittest
from method.HttpResquest import HttpResquest
from method.operationpyxl import operationpyxl
import os

headers = {"Content-Type": "application/json;charset=UTF-8"}
class Test_my(unittest.TestCase):
    def login(self):
        url = 'https://api.shaoziketang.com/wap/v2.8/login/data'
        data = {"mobile": "17713162100", "rand": "678123"}
        res = HttpResquest().http_request(url,data,'post')
        return res.json()['data']['token']
    def test_my(self):
        url='https://api.shaoziketang.com/wap/v2.8/user/learn'
        headers['token']=self.login()
        res= HttpResquest().http_request(url,headers,'get')
        print(res.json())
        try:
            self.assertEqual(res.json()['code'],200)
        except AssertionError as e:
            raise e