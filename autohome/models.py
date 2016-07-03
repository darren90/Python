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

# CalBeatiful
class User(object):
    def __init__(self,title,detail_url,icon_url,bbs_id,bbs_name,sub_title,bbs_url):
        self.title = title
        self.detail_url = detail_url
        self.icon_url = icon_url
        self.bbs_id = bbs_id
        self.bbs_name = bbs_name
        self.sub_title = sub_title
        self.bbs_url = bbs_url

    def save(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "INSERT into CalBeatiful (title,detail_url,icon_url,bbs_id,bbs_name,sub_title,bbs_url) values (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(self.title,self.detail_url,self.icon_url,self.bbs_id,self.bbs_name,self.sub_title,self.bbs_url))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def query_all():
        conn = get_conn()
        cursor = conn.cursor()
        sql = "SELECT * from CalBeatiful"
        cursor.execute(sql)
        rows = cursor.fetchall()
        users = []
        for row in rows:
            user = User(row[0],row[1])
            users.append(user)
        conn.commit()
        cursor.close()
        conn.close()
        return users

    def __str__(self):
        return "id:{}-name:{}".format(self.title,self.detail_url)