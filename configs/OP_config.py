#encoding:utf-8
import configparser

a=configparser.ConfigParser()
a.read('test_case.config',encoding='utf-8')
print(a.get('PEOPLE','name'))