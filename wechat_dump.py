#!/user/bin/python3
# -*- coding:utf-8 -*-
# Author :liqi

from wxpy import *

def mess_dump():

    bot = Bot() # 扫码登陆
    # bot.friends() 获取所有好友
    friends=bot.friends() #返回结果为一个chats（列表） 对象
    stats=friends.stats()
    stats_te = friends.stats_text()#获取好友的分布情况
    print(friends)
    print(stats)
    print("==========\n"stats_te)

    # bot.groups() 获取所有群聊对象
    print(bot.groups())
    #bot.mps() 获取所有公众号
    print(bot.mps())
    #bot.chats() 获取所有聊天对象
    print(bot.chats())
   # f = open('G:/test/wachat.txt','ab')
  #  f.write(bot.friends())
  #  f.write(bot.groups())
  #  f.write(bot.mps())
  #  f.write(bot.chats())
  #  f.close()

mess_dump()


