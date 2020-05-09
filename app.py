import os

from flask import *


from blueprints.interface import interface
from blueprints.panes import panes
from blueprints.api import api
import db

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'dev',
    SQLALCHEMY_DATABASE_URI=os.environ["DATABASE_URL"],
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    TEMPLATES_AUTO_RELOAD=True
)

# app.config['TEMPLATES_AUTO_RELOAD'] = True

db.init_app_db(app)

app.register_blueprint(interface, url_prefix="/")
app.register_blueprint(panes, url_prefix="/panes")
app.register_blueprint(api, url_prefix="/api")

if __name__ == '__main__':
    app.run()
