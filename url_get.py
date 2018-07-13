#!/user/bin/python3
# -*- coding:utf-8 -*-
#Author : liqi

import requests

import json
#import urllib.request


def get_daily():
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
#    print(r.json())
    note= r.json()['note']
    content= r.json()['content']
    translation = r.json()['translation']
    return content,note,translation

def url_test():
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    print(type(r))  # 类型
    print(r.status_code)  # 状态
    print(r.encoding)  # 编码方式
    print(r.cookies)  # cookies

def urlib_test():
    url = "https://api.douban.com/v2/book/isbn/"
    r = requests.get(url)
    print(r.json())
    url = "http://api.douban.com/v2/book/isbn/9787218087351"
    r = requests.get(url)
    print(r.json())
    print(r.json()['request'])
    print(r.json()['code'])




if __name__=="__main__":
    print(get_daily()[0],"--",get_daily()[1])
    print("                                                            ----",get_daily()[2][5:18])
#    url_test()
#    urlib_test()



