from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{0}:{1}@{2}/{3}'.format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)
db = SQLAlchemy(app)
