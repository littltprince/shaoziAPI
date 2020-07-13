#encoding:utf-8
import requests
class HttpResquest:
    def http_request(self,url,data,method):
        if method.lower() =='post':
            res=requests.post(url,data,verify=False)
        else:
            res=requests.get(url,data,verify=False)
        return res
# if __name__ == '__main__':
#     url='https://api.shaoziketang.com/wap/v2.8/login/data'
#     data={"mobile":"17713162100","rand":"678123"}
#
#     res=HttpResquest().http_request(url,data,'post')
#     print('url的类型是{}'.format(type(url)))
#     print('data的类型是{}'.format(type(data)))
#     print("登录结果是：",res.json())