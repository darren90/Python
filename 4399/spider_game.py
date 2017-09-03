#-*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import types
import urlparse
import sys
from Gmodels import GameNews
from Gmodels import SpiderdbModel
from Gmodels import GameNews_Content
import base64


reload(sys)
sys.setdefaultencoding("utf-8")

class spider(object):
    def __init__(self):
        print u'-- 开始爬取内容。。。'

#getsource用来获取网页源代码
    def getsource(self,url):
        print '待爬取url:%s' %url
        print ''
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
       print u'--1 开始爬取标题，图片。。。。。。'
       links_arary = [] #set()
       for page_url in all_pages:
           if page_url is None:
             break
           html = mySpider.getsource(page_url)
           if html is None:
             continue
           # print 'start-- : %s ' % html


             # 都不为空的时候，存储爬取的链接
           isHadSpider = SpiderdbModel.isThisHadSpider(page_url, html)
           # print '---url:%s,hadSpider:%d'%(url,isHadSpider)
           if isHadSpider == True:
               print '地址：%s 已经爬取，并且内容没有更新' % page_url
               continue
           else:
               print '地址：%s 没有爬取' % page_url
               SpiderdbModel.saveSpider(page_url, html)


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

                gNews = GameNews(title, jump_url_s, img_url, brief,'')
                gNews.save()
                links_arary.append(gNews)

       return links_arary

# 爬去网页的内容的详情
    def get_url_content(self , all_content_links):
        print u'--2 开始爬取详情网页。。。。。。:%d' % len(all_conetnt_links)
        for gmodel in all_content_links:
            # print (gmodel.detail_url)
            if gmodel.detail_url is None:
                continue
            html_content = mySpider.getsource(gmodel.detail_url)
            if html_content is None:
                continue

            soup = BeautifulSoup(html_content, "html.parser")
            div_content = soup.find('div', class_="pleft-txt")
            if div_content != None:
                con = div_content.prettify()	# 直接获取所有内容
                # print (type(con))

                # update 数据库
                contentModel = GameNews_Content(gmodel.detail_url, con)
                # gmodel.detail_content = con
                contentModel.save()
                # print gmodel

if __name__ == '__main__':

    url = 'http://news.4399.com/gonglue/wzlm/zixun/44038-' # http://news.4399.com/gonglue/wzlm/zixun/44038-1.html
    mySpider = spider()
    all_pages = mySpider.get_all_pages(url,50) #所有的页面 50
    all_conetnt_links = mySpider.get_all_urls(all_pages)
    mySpider.get_url_content(all_conetnt_links)





