from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_json_schema import JsonSchema

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@127.0.0.1/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

schema = JsonSchema(app)

from flaskApp.utils import logger
from flaskApp.routes import student, department