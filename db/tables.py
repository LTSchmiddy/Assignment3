from datetime import datetime
from db import dba
from flask_sqlalchemy import SQLAlchemy
import json

from datetime import datetime



def datetime_html_to_py(value: str):
    pass

def datetime_py_to_html(value: datetime):
    return f"{value.year}-{value.month:02}-{value.day:02}T{value.hour:02}:{value.minute:02}"

def time_py_to_html(value: datetime):
    return f"{value.hour:02}:{value.minute:02}"

def date_py_to_html(value: datetime):
    return f"{value.year}-{value.month:02}-{value.day:02}"

class TodoItem(dba.Model):
    __tablename__ = 'todo'
    id = dba.Column(dba.Integer, primary_key=True, autoincrement=1)
    title = dba.Column(dba.Text, nullable=False)
    description = dba.Column(dba.Text)
    date_added = dba.Column(dba.TIMESTAMP, nullable=False)
    date_due = dba.Column(dba.TIMESTAMP)
    completed = dba.Column(dba.Boolean, nullable=False, default=False)

    @staticmethod
    def get_next_key():
        highest = TodoItem.query.order_by(TodoItem.id.desc()).first()

        if highest is None:
            return 1

        return TodoItem.query.order_by(TodoItem.id.desc()).first().id + 1

    def get_date_due_html(self):
        if self.date_due is None:
            return None

        return datetime_py_to_html(self.date_due)

    def get_date_due_date_html(self):
        if self.date_due is None:
            return None

        return date_py_to_html(self.date_due)

    def get_date_due_time_html(self):
        if self.date_due is None:
            return None

        return time_py_to_html(self.date_due)



    class JSONEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, TodoItem):
                return {
                    'id': o.id,
                    'title': o.title,
                    'description': o.description,
                    'date_added': o.date_added,
                    'date_due': o.date_due,
                    'completed': o.completed,
                }

            # return super(json.JSONEncoder, self).default(o)