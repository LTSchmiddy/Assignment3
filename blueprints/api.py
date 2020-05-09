import os
from flask import Blueprint, request
import sqlalchemy
from db.tables import *

from datetime import datetime
import json

api = Blueprint(
    'api',
    __name__,
    root_path=os.getcwd(),
    template_folder="api_templates",
    static_folder="static",
)

@api.route("/list_ids", methods=('GET', 'POST'))
def list_id():
    all_todos = TodoItem.query.all()

    retVal = []
    for i in all_todos:
        retVal.append(i.id)

    return json.dumps(retVal)

@api.route("/list_full", methods=('GET', 'POST'))
def list_entries():
    all_todos = TodoItem.query.all()

    retVal = []
    for i in all_todos:
        retVal.append(i)

    return json.dumps(retVal, cls=TodoItem.JSONEncoder)



@api.route("/create", methods=('GET', 'POST'))
def create_entry():
    entry: TodoItem = TodoItem(
        id=TodoItem.get_next_key(),
        title="New Todo Item",
        date_added=datetime.now()
    )

    dba.session.add(entry)
    dba.session.commit()

    return str(entry.id)


@api.route("/read", methods=('GET', 'POST'))
def read_entry():
    return json.dumps(TodoItem.query.filter(TodoItem.id == request.form.get('id')).first(), cls=TodoItem.JSONEncoder)


@api.route("/write", methods=('GET', 'POST'))
def update_entry():
    print(request.form)



    entry: TodoItem = TodoItem.query.filter(TodoItem.id == request.form.get('id')).first()

    entry.title = request.form.get('title')
    entry.description = request.form.get('description')

    r_date_due = request.form.get('date_due')

    try:
        if r_date_due == "" or r_date_due == "None" or r_date_due == "T":
            entry.date_due = None

        else:
            entry.date_due = r_date_due

    except sqlalchemy.exc.DataError as e:
        entry.date_due = None

    entry.completed = (request.form.get('completed') == 'true')

    dba.session.commit()

    return "saved"


@api.route("/delete", methods=('GET', 'POST'))
def delete_entry():
    dba.session.delete(TodoItem.query.filter(TodoItem.id == request.form.get('id')).first())
    dba.session.commit()
    return "deleted"