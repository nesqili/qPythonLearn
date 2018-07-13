#!/usr/bin/python3
# -*- coding:utf-8 -*-
##获取网页的精美图片,并保存到本地
from requests_html import HTMLSession
import requests
import time

session = HTMLSession()

def get_picture_list(html):
    response = session.get(html) #获取一个HTML窗口
    content = response.html.find('div.Left_bar',first=True) #找到div class="Left_bar"这一项
    li_list=content.find('li')   #找到里面的li  ，即是所有的图片信息项，包括名称和链接以及说明
    for li in li_list:
        url = li.find('a',first=True).attrs['href']  #获取li的二级链接URL
        print(url)
        get_picure_detail(url)

def get_picure_detail(url):
    response = session.get(url)
    content = response.html.find('div.scroll-img-cont',first=True)
    li_list = content.find('li')
    for li in li_list:
        img_url = li.find('img',first=True).attrs['data-original']
        img_url = img_url[0:img_url.find('_')] + '.jpg'
        print(img_url + '.jpg')        # picture url
        save_image(img_url)

def save_image(img_url):
    img_response = requests.get(img_url)
    t = int(round(time.time()*1000))
   # print(t)  ## time
    f = open('G:/test/%d.jpg' % t,'ab')
    f.write(img_response.content)
    f.close()

if __name__=='__main__':
#    html='http://www.win4000.com/zt/xinggan.html'
    html='http://www.win4000.com/zt/xiaoqingxin.html'
    get_picture_list(html)