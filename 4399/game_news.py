#-*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import types
import urlparse
import sys
from Gmodels import GameNews

reload(sys)
sys.setdefaultencoding("utf-8")

class spider(object):
    def __init__(self):
        print u'-- 开始爬取内容。。。'

#getsource用来获取网页源代码
    def getsource(self,url):
        print '待爬取url:%s' %url
        response = requests.get(url)
        response.encoding = 'gb2312'
        return response.text

#得到所有的待爬取的链接
    def get_all_pages(self,url,total_page):
        pages_arary = []
        count = 1
        for i in range(1,total_page):
            new_url = '%d' % count + ".html"
            new_full_url = url + new_url
            # print new_full_url
            pages_arary.append(new_full_url)
            count = count + 1
        return pages_arary
        
# 获取每个页面待爬取的item具体内容的链接
    def get_all_urls(self,all_pages):
       links_arary = [] #set()
       for page_url in all_pages:
           if page_url is None:
             break
           html = mySpider.getsource(page_url)
           if html is None:
             break
           # print 'start-- : %s ' % html
           soup = BeautifulSoup(html, "html.parser")
           ul_all = soup.find('ul',class_="txt-list cf")
           for link in ul_all.find_all('li'):
                title_s = link.find('div', class_="tl-tit cf")
                # 标题
                title = title_s.find('a').get_text()
                # print title
                # 图片地址
                img_s = link.find('div', class_="tl-img cf")
                img_url = img_s.find('a').find('img')['src']

                # 链接
                jump_url = img_s.find('a')['href']
                jump_url_s = urlparse.urljoin("http://news.4399.com", jump_url)

                # 简介
                brief = img_s.find('p').get_text()

                gNews = GameNews(title, jump_url_s, img_url, brief)
                gNews.save()

       return links_arary

if __name__ == '__main__':
    # fout = open('output_dy.sql','w')
    fialCount = 1
    count = 1
    classinfo = []
    url = 'http://news.4399.com/gonglue/wzlm/zixun/44038-' # http://news.4399.com/gonglue/wzlm/zixun/44038-1.html
    mySpider = spider()
    all_pages = mySpider.get_all_pages(url,50) #所有的页面 50
    all_links = mySpider.get_all_urls(all_pages)
    # fout.close()
 





