#encoding:utf-8
import pymysql
import requests

# 打开数据库连接
db = pymysql.connect("rm-2ze6g25687k3mjso64o.mysql.rds.aliyuncs.com",
                     "shaozi2016", "XLyNF4I0TQA9YXZf", "db_test")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
query_sql='select  content from sz_message where mobile="17713162100" order by created_at desc limit 1'
cursor.execute(query_sql)

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print(data[0],type(data[0]))
# print(data)
# print(type(data))

# 关闭数据库连接
db.close()
@classmethod
class Get_code():
    code=getattr('Get_code','code',data[0])
# if __name__ == '__main__':
#     print(Get_code,type(Get_code))
def login():
    url='https://api.shaoziketang.com/wap/v2.8/data/login'
    data={"mobile":"15312362160","rand":Get_code.code}
    res=requests.post(url,data)
    print(res.json())
if __name__ == '__main__':
    login()