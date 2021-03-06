#-*- coding: UTF-8 -*-

import  MySQLdb
import hashlib

try:
    import cPickle as pickle
except ImportError:
    import pickle


import HTMLParser


def get_conn():
    host = "127.0.0.1"
    port = 3306
    db = "fei"
    user = "root"
    password = "root"
    conn = MySQLdb.connect(host = host,
                           user = user,
                           passwd = password,
                           db = db,
                           port = port,
                           charset = "utf8")
    return conn






# GameNews
class GameNews(object):
    # def __init__(self,title,detail_url,icon_url,sub_title):
    #     self.title = title
    #     self.detail_url = detail_url
    #     self.icon_url = icon_url
    #     self.sub_title = sub_title

    def __init__(self,title,detail_url,icon_url,sub_title):
        self.title = title
        self.detail_url = detail_url
        self.icon_url = icon_url
        self.sub_title = sub_title
        self.idStr = 0


    def save(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql_sel = "select * from GameNews where title = \'%s\' and detail_url = \'%s\' ;" % (self.title,self.detail_url)
        cursor.execute(sql_sel)
        rows = cursor.fetchall()
        # 判断是否已经储存过
        if len(rows) != 0:
            # print '---YES--这一条已经爬取-：%s-' % self.title
            return

        sql = "INSERT into GameNews (title,detail_url,icon_url,sub_title) values (%s,%s,%s,%s)"
        cursor.execute(sql,(self.title,self.detail_url,self.icon_url,self.sub_title))
        conn.commit()
        cursor.close()
        conn.close()

    def get_gameNews_id(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql_sel = "select id from GameNews where title = \'%s\' and detail_url = \'%s\' ;" % (self.title,self.detail_url)
        # print sql_sel
        cursor.execute(sql_sel)
        rows = cursor.fetchall()

        result_id = 0
        if len(rows) != 0:
            result_id = int(rows[0][0])

        cursor.close()
        conn.close()
        return  result_id


    # 废弃
    def upate(self):
        conn = get_conn()
        cursor = conn.cursor()
        # self.detail_content = MySQLdb.escape_string(self.detail_content.encode('utf-8'))
        # print '---detail ' + self.detail_content

        # detail_blob = pickle.dumps(self.detail_content, protocol=1)
        # print '--:detail_blob : ' + detail_blob
        # sql_sel = "select * from GameNews where title = \'%s\' and detail_url = \'%s\' ;" % (self.title,self.detail_url)
        # cursor.execute(sql_sel)
        # rows = cursor.fetchall()
        # # 判断是否已经储存过
        # if len(rows) != 0:
        #     # print '---YES--这一条已经爬取-：%s-' % self.title
        #     return
        sql = "UPDATE GameNews set detail_blob = \'%s\' where title = \"%s\" AND detail_url = \"%s\" ;" % (self.detail_content,self.title,self.detail_url)
        print '--:sql: %s' % sql
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()


    @staticmethod
    def query_all():
        conn = get_conn()
        cursor = conn.cursor()
        sql = "SELECT * from GameNews"
        cursor.execute(sql)
        rows = cursor.fetchall()
        users = []
        for row in rows:
            user = GameNews(row[0],row[1])
            users.append(user)
        conn.commit()
        cursor.close()
        conn.close()
        return users


    @staticmethod
    def query_all(page):
        count = 15
        conn = get_conn()
        cursor = conn.cursor()
        sql = "SELECT title,detail_url,icon_url,sub_title,id from GameNews order by id asc limit %d,%d" % ((page - 1)*count, count)
        print sql
        cursor.execute(sql)
        rows = cursor.fetchall()
        users = []
        for row in rows:
            user = GameNews(row[0],row[1],row[2],row[3])
            user.idStr = row[4]
            # user_json = user.to_json()
            users.append(user)
        conn.commit()
        cursor.close()
        conn.close()
        return users

    def to_json(self):
        return {
            'idStr': self.idStr,
            'title': self.title,
            'detail_url': self.detail_url,
            'icon_url': self.icon_url,
            'sub_title': self.sub_title,
        }

    def __str__(self):
        return "id:{}-name:{}".format(self.title,self.detail_url)



class GameNews_Content(object):
    def __init__(self,idStr,url,detail_content):
        self.idStr = idStr
        self.url = url
        self.detail_content = detail_content

    def save(self):
        self.detail_content = MySQLdb.escape_string(self.detail_content.encode('utf-8'))

        conn = get_conn()
        cursor = conn.cursor()
        sql = "INSERT into GameNews_Content (idStr, url,detail_content) values (%d ,\"%s\" ,\"%s\" )" % (self.idStr,self.url,self.detail_content)
        # print sql
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def query_content(idStr):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "select detail_content from GameNews_Content where idStr = \"%s\" ;" % (idStr)
        print '-query_content-:sql: %s' % sql
        content = ""
        cursor.execute(sql)
        rows = cursor.fetchall()
        if len(rows) != 0:
            content = rows[0][0]

        cursor.close()
        conn.close()
        html_parser = HTMLParser.HTMLParser()
        newtitle = html_parser.unescape(content)
        # newtitle = newtitle.replace('\n','<br/>') #&nbsp
        # newtitle = MySQLdb.escape_string(content.encode('utf-8'))
        print newtitle
        return newtitle

    def to_json(self):
        return {
            'idStr' : self.idStr,
            'detail_url': self.detail_url,
            'detail_content': self.detail_content,
        }



# 爬取的地址
class SpiderdbModel(object):
    def __init__(self, url, md5, content,type):
        self.url = url
        self.md5 = md5
        self.content = content
        self.type = type

    @staticmethod
    def saveSpider(url, content):
        md5_ = hashlib.md5(content.encode('utf-8')).hexdigest()

        conn = get_conn()
        cursor = conn.cursor()
        sql = "INSERT into spiderdb (url,md5,stype) values (\'%s\' ,\'%s\' ,\'%s\')" % (url, md5_, 'carCalBeatiful')
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    # 终极检验，url+md5
    @staticmethod
    def isThisHadSpider(url, content):
        md5 = hashlib.md5(content.encode('utf-8')).hexdigest()
        # print 'url:%s,md5,,%s' % (url, md5)

        conn = get_conn()
        cursor = conn.cursor()
        sql = "select * from spiderdb where md5 = \'%s\' or url = \'%s\' ;" % (md5, url)
        cursor.execute(sql)
        rows = cursor.fetchall()
        result = False
        if len(rows) != 0:
            result = True
        conn.commit()
        cursor.close()
        conn.close()
        return result

    # @staticmethod
    # def query_all():
    #     conn = get_conn()
    #     cursor = conn.cursor()
    #     sql = "SELECT url, md5 from spiderdb"
    #     cursor.execute(sql)
    #     rows = cursor.fetchall()
    #     spiderdbs = []
    #     for row in rows:
    #         spiderdb = SpiderdbModel(row[0], row[1]])
    #         spiderdbs.append(spiderdb)
    #     conn.commit()
    #     cursor.close()
    #     conn.close()
    #     return spiderdbs









