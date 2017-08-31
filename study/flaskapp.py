#-*- coding: UTF-8 -*-

from flask import Flask,render_template,flash,abort
from model import User
import request
from flask import request

app = Flask(__name__)
app.secret_key = "123"

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/users/<id>')
def user_id(id):
    return 'hello world:' + id

@app.route('/query_user' , methods=['GET'])
def query_user():
    id = request.args.get('id')
    return 'query user:' + id

# 动态内容

@app.route('/con')
def con():
    content = 'tengfei'
    return render_template("index.html", content = content)

@app.route('/user')
def user_index():
    user = User(1, 'jikexuey')
    return render_template("user_index.html", user = user)

@app.route('/userid/<userid>')
def userid(userid):
    user = None
    if int(userid) == 1:
        user = User(1,'tengfei')
    return  render_template('userid_index.html', user = user)

@app.route('/users')
def user_list():
    users = []
    for i in range(1, 11):
        user = User(i, 'jikexueyuan'+str(i))
        users.append(user)
    return render_template('users.html',users = users)

# 模板的继承

@app.route('/one')
def one():
    return render_template("con_base.html")

@app.route('/two')
def two():
    return render_template("con_base2.html")


# 消息提示语异常处理


@app.route('/mes')
def mes():
    flash("wrong")
    return render_template("news.html")



@app.route('/loginss',methods=['POST'])
def loginss():
    form = request.form
    user_name = form.get('username')
    password = form.get('password')
    if not user_name:
        flash("no Username")
        return render_template("news.html")
    if not password:
        flash("no Password")
        return render_template("news.html")

    if user_name == '123' and password == '123':
        flash("success")
        return render_template("news.html")
    else:
        flash("wrong")
        return render_template("news.html")


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@app.route('search/<user_id>')
def searchh(user_id):
    if int(user_id) == 1:
        return abort(404)






















if __name__ == '__main__':
    app.run()