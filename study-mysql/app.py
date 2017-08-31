from flask import Flask
from models import  User

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

def save():
    user = User(1, 'jikexueyuan')
    user.save()


def query():
    User.query_all()


if __name__ == '__main__':
    save()
    app.run()
