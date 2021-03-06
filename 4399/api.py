#-*- coding: UTF-8 -*-

#!flask/bin/python
from flask import Flask, jsonify,abort
from bs4 import BeautifulSoup
import requests
import re
import types
import urlparse
import sys
from Gmodels import GameNews
from Gmodels import GameNews_Content

reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)



@app.route('/')
def index():
    return "hello tengfei"

@app.route('/error')
def not_found():
    print '404 not found'
    return jsonify({'error': 'Not found'})

@app.route('/list/<page>')
def get_list(page):
    games = GameNews.query_all(int(page))
    # return jsonify(data=games)
    return  jsonify(status="success",datas=[game.to_json() for game in games])

@app.route('/html_content/<idStr>')
def get_html_content(idStr):
    content = GameNews_Content.query_content(idStr)
    return  jsonify(status="success",data={'content' : content})









tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)