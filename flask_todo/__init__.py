from datetime import datetime

from flask import Flask, request, render_template, redirect

from . import items
from . import db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DB_USER='csetuser',
        DB_NAME='todo_objects',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    db.init_app(app)

    @app.route('/', methods=['GET'])
    def index():
        # in handler, we'll have to probably make a list for now so to-do items stay over multiple post requests

        # takes query parameters
        # todo_item = request.args.get('todo', 'none')
        # display regular todo list if no query parameter
        conn = db.get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM todo_list;")
        todo = cur.fetchall()

        return render_template('index.html', todo=todo)

        #todo.append(items.Item(request.form.get("todo")))
        #return render_template('index.html', todo=todo)
        # if todo_item = 'none':
        # return return_template('index.html')
        # if query param name matches name of todo item, display only todo item
        # if query param is completed, displays only completed items

    @app.route('/add', methods=['GET', 'POST'])
    def add():

        if request.method == 'GET':
            return render_template('add.html')

        elif request.method == 'POST':
            new_item = items.Item(request.form.get("todo"))
            conn = db.get_db()
            cur = conn.cursor()

            cur.execute("""
                INSERT INTO todo_list (task, tstamp, is_completed)
                VALUES (%s, %s, %s);
                """,
                (new_item.job, new_item.timestamp, new_item.is_complete)
            )

            conn.commit()


            return render_template('add.html')

    @app.route('/complete', methods=['GET', 'POST'])
    def complete():
        if request.method == 'GET':
            conn = db.get_db()
            cur = conn.cursor()

            cur.execute("SELECT * FROM todo_list WHERE is_completed = false;")
            todo = cur.fetchall()

            return render_template('complete.html', todo=todo)

        elif request.method == 'POST':

            postID = request.form.get("selector")

            conn = db.get_db()
            cur = conn.cursor()

            cur.execute("""
                UPDATE todo_list SET is_completed = true
                WHERE id = %s
                """,
                (postID)
            )
            conn.commit()

            return redirect('/')

    return app
