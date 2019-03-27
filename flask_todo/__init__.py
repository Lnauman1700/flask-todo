from datetime import datetime

from flask import Flask, request, render_template

from . import items

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    todo = []

    @app.route('/', methods=['GET', 'POST'])
    def index():
        # in handler, we'll have to probably make a list for now so to-do items stay over multiple post requests

        # takes query parameters
        # todo_item = request.args.get('todo', 'none')
        # display regular todo list if no query parameter
        if request.method == 'GET':
            return render_template('index.html')

        elif request.method == 'POST':
            todo.append(items.Item(request.form.get("todo")))
            return render_template('index.html', todo=todo)
        # if todo_item = 'none':
        # return return_template('index.html')
        # if query param name matches name of todo item, display only todo item
        # if query param is completed, displays only completed items


    return app
