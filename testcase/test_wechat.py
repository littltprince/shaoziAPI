# # -*- coding: utf-8 -*-
# '''
# @author: haffner2010
# @contact: myprojtest@163.com
# @Software: Pycharm + Python3.6
# @OS:Windows 10 64 bit
# @Site:https://allbluelai.github.io
# @file: wx_delete_friend.py
# @time: 2018/9/11 19:05
# @desc:清除微信中无效的好友
# '''
#
# from wxpy import *
# from time import sleep
# from functools import reduce
#
#
# # 登陆
# bot = Bot(cache_path=True) # 缓存登陆信息,使用默认的缓存路径 'wxpy.pkl'
# # bot = Bot()
# bot.file_helper.send('hello world!')
# # 获取所有好友
# friends = bot.friends()
# friends.pop(0) # 清除自己
# except_list = ['user1','user2'] # 排除不需要测试的好友,可以为空
# if except_list:
#     except_friends=list(map(friends.search,except_list))
#     except_friends = reduce(lambda x, y: x+ y, except_friends)
# else:
#     except_friends=[]
# print(except_friends)
# for friend in friends:
#     if friend not in except_friends:
#         # 发送文本，判断好友是否把你拉黑或者删除
#         try:
#             # print(friend)
#             # https://www.douban.com/note/665907454/
#             friend.send('ॣ ॣ ॣ')
#             sleep(2) # 控制发送消息的频率
#             # print('succeed!')
#         except exceptions.ResponseError as e:
#             bot.file_helper.send(f'{friend}:{e}')
# embed()