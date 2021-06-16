from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import server_secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(server_secrets.dbuser, server_secrets.dbpass, server_secrets.dbhost, server_secrets.dbname)
db = SQLAlchemy(app)
