import  MySQLdb

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
    def __init__(self,title,detail_url,icon_url,sub_title):
        self.title = title
        self.detail_url = detail_url
        self.icon_url = icon_url
        self.sub_title = sub_title

    def save(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "INSERT into GameNews (title,detail_url,icon_url,sub_title) values (%s,%s,%s,%s)"
        cursor.execute(sql,(self.title,self.detail_url,self.icon_url,self.sub_title))
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
        count = 20
        conn = get_conn()
        cursor = conn.cursor()
        sql = "SELECT title,detail_url,icon_url,sub_title from GameNews order by id asc limit %d,%d" % (page*count, page*(1+count))
        cursor.execute(sql)
        rows = cursor.fetchall()
        users = []
        for row in rows:
            user = GameNews(row[0],row[1],row[2],row[3])
            user_json = user.to_json()
            users.append(user_json)
        conn.commit()
        cursor.close()
        conn.close()
        return users

    def to_json(self):
        return {
            'title': self.title,
            'detail_url': self.detail_url,
            'icon_url': self.icon_url,
            'sub_title': self.sub_title,
        }

    def __str__(self):
        return "id:{}-name:{}".format(self.title,self.detail_url)