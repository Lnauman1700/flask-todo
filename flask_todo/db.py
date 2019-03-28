import psycopg2

from flask import current_app, g
from flask.cli import with_appcontext

def get_db():

    if 'db' not in g:
        g.db = psycopg2.connect("dbname=todo_objects user=csetuser")

    return g.db

def close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()

def new_db():
    # should drop tables and make them anew
