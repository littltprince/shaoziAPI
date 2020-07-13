#encoding utf-8
from openpyxl import load_workbook
import os
base_dir=os.path.dirname(os.path.dirname(__file__))
data_path=os.path.join(base_dir,'data/ddt_data.xlsx')
class operationpyxl:
    def __init__(self,path,sheet_name):
        self.path=path
        self.sheet_name=sheet_name
    def get_data(self):
        a=load_workbook(self.path)
        sheet=a[self.sheet_name]
        # print(sheet.max_row)
        # print(sheet.max_column)
        test_data=[]
        for i in range(2,sheet.max_row+1):#从第2行开始取值
            sub_data = {}
            sub_data["case_id"]=sheet.cell(i,1).value
            sub_data["title"] = sheet.cell(i,2).value
            sub_data["url"] = sheet.cell(i,3).value
            sub_data["data"] = sheet.cell(i,4).value
            sub_data["method"] = sheet.cell(i,5).value
            sub_data["expect"] = sheet.cell(i,6).value
            sub_data["fact"] = sheet.cell(i,7).value
            test_data.append(sub_data)
        return test_data

# if __name__ == '__main__':
#     print(operationpyxl(data_path,'sheet1').get_data())


