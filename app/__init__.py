from flask import Flask, url_for
from flask.ext.sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
from app import views, models
