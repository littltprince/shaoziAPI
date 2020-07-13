#encoding:utf-8
import configparser
import os
basePath=os.path.dirname(os.path.dirname(__file__))
filePath=os.path.join(basePath,'configs/test_case.config')
#config下的数据类型都是str，可以利用eval来进行数据转换
class opconfig():
    def OpConfig(self,ConfigName,ModeName,SectionName):
        a = configparser.ConfigParser()
        a.read(ConfigName, encoding='utf-8')
        return a.get(ModeName,SectionName)

# if __name__ == '__main__':
#     print(opcongif().OpConfig(filePath,'PEOPLE','test_num'))