# app.py
from flask import Flask
from flask_cors import CORS  # Import the CORS extension
import argparse
import argsss
import ossss
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:sa123@127.0.0.1/codecrafter"
db = SQLAlchemy(app)
@app.route('/')
def hello_world():
    return 'Hello, World!hgh'
my changes
@app.route("/name/<name>",methods=['GET'])
def saymyname(name):
    return f"Hii {name}"
@app.route("/create_jira", methods=['POST'])
def create_jira():
    data = request.get_json()
    # code to create a new jira issue with the data
    from jira import JIRA
    # Create a connection object
    jira = JIRA(basic_auth=('username', 'password'), options={'server': 'https://your_jira_server_url'})
    # Create an issue
    issue_dict = {
        'project': {'key': data['project_key']},
        'summary': data['summary'],
        'description': data['description'],
        'issuetype': {'name': data['issue_type']},
    }
    issue = jira.create_issue(fields=issue_dict)
    return 'Jira issue created successfully'

parser = argparse.ArgumentParser(description="Run Flask application")
parser.add_argument('-p', '--port', type=int, default=5000, help='Port to run the app on')
args = parser.parse_args()
port = args.port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
