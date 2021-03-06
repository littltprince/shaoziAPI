import unittest
import requests
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
        res = HttpResquest().http_request(item['url'],item['data'],item['method'],headers=headers)
        # res=requests.get(item['url'],headers)
        print(res.json())
        operationpyxl(file_path,'my').write_fact(item['case_id'] + 1,res.json()['code'])
        try:
            self.assertEqual(res.json()['code'],200)
            operationpyxl(file_path, 'my').write_result(item['case_id'] + 1, 'pass')
        except AssertionError as e:
            operationpyxl(file_path, 'my').write_result(item['case_id'] + 1, 'Failed')
            raise e
        # finally:
        #     operationpyxl(file_path, 'my').write_result(item['case_id'] + 1, str(res.json()))
