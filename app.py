# app.py
from flask import Flask
from flask_cors import CORS  # Import the CORS extension
import argparse
import os

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:sa123@127.0.0.1/codecrafter"
db = SQLAlchemy(app)
@app.route('/')
def hello_world():
    return 'Hello, World!hgh'
@app.route("/name/<name>",methods=['GET'])
def saymyname(name):
    return f"Hii {name}"
parser = argparse.ArgumentParser(description="Run Flask application")
parser.add_argument('-p', '--port', type=int, default=5000, help='Port to run the app on')
args = parser.parse_args()
port = args.port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
