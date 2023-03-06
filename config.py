from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:56465646@localhost/portfolio'
app.config['SQLALCHEMY_DATABASE_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "dc01bdafd5c9c3393911fa8b"
app.config['FLASK_DEBUG'] = True


'''create an instance of SQLAlchemy database'''
db = SQLAlchemy()
'''register the Flask app instance with the SQLAlchemy'''
db.init_app(app) 