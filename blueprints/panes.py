import os
from flask import *
from db.tables import *

panes = Blueprint(
    'panes',
    __name__,
    root_path=os.getcwd(),
    template_folder="templates/pane_templates",
    static_folder="static",
)


@panes.route('/item_list', methods=('GET', 'POST'))
def item_list():
    return render_template("item_button_list.html", items=TodoItem.query.order_by(TodoItem.date_added).all())


@panes.route('/item_view', methods=('GET', 'POST'))
def item_view():
    print()

    search_id = request.form.get('id')
    return render_template("item_view.html", item=TodoItem.query.filter(TodoItem.id == search_id).first())