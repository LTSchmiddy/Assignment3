from flask import jsonify
from flask.cli import with_appcontext
# from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import *

dba = SQLAlchemy()

from db.tables import *
import json

def init_app_db(app):
    with app.app_context():
        dba.init_app(app)
        dba.create_all()