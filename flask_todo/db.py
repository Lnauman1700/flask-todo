import psycopg2

from flask import current_app, g
from flask.cli import with_appcontext

def get_db():

    g.db = psycopg2.connect()
