from datetime import datetime

from flask import Flask, request, render_template, redirect
import psycopg2

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

    db = psycopg2.connect("dbname=todo_objects user=csetuser")

    @app.route('/', methods=['GET'])
    def index():
        # in handler, we'll have to probably make a list for now so to-do items stay over multiple post requests

        # takes query parameters
        # todo_item = request.args.get('todo', 'none')
        # display regular todo list if no query parameter
        cur = db.cursor()
        cur.execute("SELECT * FROM todo_list;")
        return render_template('index.html', todo=cur.fetchall())

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
            cur = db.cursor()

            cur.execute("""
                INSERT INTO todo_list (task, tstamp, is_completed)
                VALUES (%s, %s, %s);
                """,
                (new_item.job, new_item.timestamp, new_item.is_complete)
            )

            db.commit()

            return render_template('add.html')

    @app.route('/complete', methods=['GET', 'POST'])
    def complete():
        if request.method == 'GET':
            cur = db.cursor()

            cur.execute("SELECT * FROM todo_list WHERE is_completed = false;")

            return render_template('complete.html', todo=cur.fetchall())

        elif request.method == 'POST':

            postID = request.form.get("selector")
            cur = db.cursor()

            cur.execute("""
                UPDATE todo_list SET is_completed = true
                WHERE id = %s
                """,
                (postID)
            )
            db.commit()
            
            return redirect('/')

    return app
