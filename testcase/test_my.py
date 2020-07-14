import unittest
from ddt import ddt,unpack,data
from method.HttpResquest import HttpResquest
from method.operationpyxl import operationpyxl
import os
base_path=os.path.dirname(os.path.dirname(__file__))
file_path=os.path.join(base_path,'data/ddt_data.xlsx')
test_data=operationpyxl(file_path,'my').get_data()
headers = {"Content-Type": "application/json;charset=UTF-8"}
@ddt
class Test_my(unittest.TestCase):
    def login(self):
        url = 'https://api.shaoziketang.com/wap/v2.8/login/data'
        data = {"mobile": "17713162100", "rand": "678123"}
        res = HttpResquest().http_request(url,data,'post')
        return res.json()['data']['token']
    @data(*test_data)
    def test_my(self,item):
        headers['token']=self.login()
        res= HttpResquest().http_request(item['url'],headers,'get')
        print(res.json())
        try:
            self.assertEqual(res.json()['code'],200)
        except AssertionError as e:
            raise e
