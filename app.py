# coding: UTF-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask
from models import db
from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)

app.config['DEBUG'] = True

app.secret_key = 'pass'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pass@mysql:3306/db'
app.config['SQLALCHEMY_NATIVE_UNICODE'] = 'utf-8'
db.init_app(app)
db.app = app

@app.route('/')
def hello_world():
  return 'Flask Dockerized'

@app.route('/v1/<user_geocode>/', methods=['GET'])
def get_file(user_geocode):
  return user_geocode

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host='localhost', port='5000'))

if __name__ == '__main__':
    manager.run()
