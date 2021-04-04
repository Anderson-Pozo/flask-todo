import mysql.connector
import click
from flask import current_app, g as global_context
from flask.cli import with_appcontext
from .schema import instructions


def get_db():
    if 'db' not in global_context:
        global_context.db = mysql.connector.connect(
            host=current_app.config['DATABASE_HOST'],
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASSWORD'],
            database=current_app.config['DATABASE'],
        )
        global_context.cursor = global_context.db.cursor(dictionary=True)
    return global_context.db, global_context.cursor


def close_db(e=None):
    db = global_context.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db, cursor = get_db()

    for instruction in instructions:
        cursor.execute(instruction)
    db.commit()


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized database')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
