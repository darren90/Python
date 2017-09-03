from fabric.api import  *

env.hosts = ['115.159.120.152']
env.user = 'ubuntu'
env.password = 'Tengfei90@'


def hello():
    print "hello world"


def deploy():
    with cd('home/ubuntu/Python/4399'):
        run('git pull')
        sudo('supervisorctl restart game_api')
        sudo('supervisorctl status')