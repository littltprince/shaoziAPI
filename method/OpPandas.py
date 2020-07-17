#encoding:utf-8
# import pandas as pd
# import xlrd
# import os
# filepath=os.path.join(os.path.dirname(os.path.dirname(__file__)),'data/ddt_data.xlsx')
# a=pd.read_excel(filepath,'my')
# '''pandas 对Excel的读取iloc[row,columns]'''
# print(a.iloc[[0,1],[0,1]])
import logging
#生成斐波那契数列的前20个数
list1=[1,1]
while len(list1)<20:
    i=list1[-1]+list1[-2]
    list1.append(i)
print(list1,'\n',len(list1))

#输出100以内所有的素数。


