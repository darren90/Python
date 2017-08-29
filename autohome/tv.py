#-*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import urlparse
from models import User

import sys
reload(sys)
sys.setdefaultencoding("gb2312")

class spider(object):
    def __init__(self):
        print u'-- 开始爬取内容。。。'

#getsource用来获取网页源代码
    def getsource(self,url):
        response = requests.get(url)
        response.encoding = 'gb2312'
        return response.text

#changepage用来生产不同页数的链接
    def changepage(self,url,total_page):
        pages_arary = []
        pages_arary.append(url)
        count = 2
        for i in range(1,total_page):
            new_url =  '%d' % count
            new_full_url = urlparse.urljoin(url,new_url)
            # print new_full_url
            pages_arary.append(new_full_url)
            count = count + 1
        return pages_arary


#解析具体的数据
    def parse_html_data(self,html_countent):
     res_array = []
     res_data = {}
     soup = BeautifulSoup(html_countent, "html.parser")
     links = soup.find('ul', class_="content")
     # print links
     if links is None:
        return []
     for link in links.find_all('li'):
        new_link = link.find('a')

        # 帖子的详情地址
        detail_url = new_link['href']

        # 帖子的标题
        title = new_link['title']
        # print title

        # 图片地址
        icon_url = new_link.find('img')['src']

        # 副标题
        sub_title = link.find('span').get_text()
        # 发帖人id
        bbs_id = link.find('dt').find('a').get_text()

        # bbs__ = link.find('dd', class_="font12NoLine").find('a')

        # 文章所在的论坛名字
        bbs_name = ""#bbs__.get_text()

        #文章所在论坛的地址
        bbs_url = ""#urlparse.urljoin("http://club.autohome.com.cn",bbs__['href'])
        user = User(title,detail_url,icon_url,bbs_id,bbs_name,sub_title,bbs_url)
        user.save()

if __name__ == '__main__':
    fialCount = 1
    count = 1
    classinfo = []
    url = 'http://club.autohome.com.cn/JingXuan/104/'
    mySpider = spider()
    all_pages = mySpider.changepage(url,20)
    # all_links = mySpider.getAllLines(all_pages)
    for link in all_pages:
        print link
        try:
            html = mySpider.getsource(link)
            mySpider.parse_html_data(html)
            count = count +1
        except Exception as e:
            if fialCount == 10200:
                # fout.close()
                break
            fialCount = fialCount + 1
            count = count +1





