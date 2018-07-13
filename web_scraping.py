#!/user/bin/python3
#- -*- coding：UTF-8 -*-

import requests

from requests_html import HTMLSession
#import requests_html

def get_test_link_from_sel(sel):
    mylist = []
    try:
        results = r.html.find(sel)
        for result in results:
            mytext = result.test
            mylink = list(result.absolute_links)[0]
            mylist.appedn((mytext,mylink))
        return mylist
    except:
        print("Error : get nothing .")
        return None

#import time
session = HTMLSession()
url="https://www.jianshu.com/p/85f4624485b9"
r=session.get(url)
print(r.html.text)  ##文本内容 r.html.text
            ##链接 r.html.links   相对链接
print(r.html.absolute_links)                    #r.html.absolute_links  绝对链接
print("Test only .")