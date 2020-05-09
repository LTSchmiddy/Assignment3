import os
from flask import *


interface = Blueprint(
    'interface',
    __name__,
    root_path=os.getcwd(),
    template_folder="templates",
    static_folder="static",
)

@interface.route('/')
def hello_world():
    return render_template("index.html")
