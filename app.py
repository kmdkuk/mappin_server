# coding: UTF-8
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  print app.url_map
  return 'Flask Dockerized'

@app.route('/v1/<user_geocode>/', methods=['GET'])
def get_file(user_geocode):
  return user_geocode

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
