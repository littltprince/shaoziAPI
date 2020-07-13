import unittest
from method.HttpResquest import HttpResquest
from method.operationpyxl import operationpyxl
import os
class Test_my(unittest.TestCase):
    def setUp(self) -> None:
        url = 'https://api.shaoziketang.com/wap/v2.8/login/data'
        data = {"mobile": "17713162100", "rand": "678123"}
        res = HttpResquest().http_request(url,data,'post')
        return res.json()['data']['token']

