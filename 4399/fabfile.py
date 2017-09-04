#-*- coding: UTF-8 -*-

from fabric.api import  *

env.hosts = ['115.159.120.152']
env.user = 'ubuntu'
env.password = 'Tengfei90@'


def hello():
    print "hello world"


# 拉去github最新代码，并且爬取最新的代码
def spider():
    with cd('/home/ubuntu/Python/4399'):
        run('git pull')
        run('phython api.py')


# 拉去github最新代码，并且重新部署api请求
def deploy():
    with cd('/home/ubuntu/Python/4399'):
        run('git pull')
        sudo('supervisorctl restart game_api')
        sudo('supervisorctl status')