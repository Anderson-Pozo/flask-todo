import functools
from flask import (
    Blueprint, flash, g, render_template, request, url_for, session, redirect
)
from werkzeug.exceptions import abort
from todo.db import get_db
from todo.auth import login_required


bluePrint = Blueprint('todo', __name__)


@bluePrint.route('/')
@login_required
def home():
    db, cursor = get_db()
    cursor.execute(
        'SELECT t.id, t.deadline, t.description, u.username, t.completed, t.created_at '
        'FROM todo t JOIN user u on t.created_by = u.id WHERE u.id=%s '
        'ORDER BY created_at DESC',
        (g.user['id'],)
    )
    todos = cursor.fetchall()
    return render_template('todo/home.html', todos=todos)


@bluePrint.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        description = request.form['description']
        deadline = request.form['deadline']
        # print('DEADLINEEEEEEEE', deadline)
        error = None
        if not description:
            error = 'Description is required'
        if error is not None:
            flash(error)
        else:
            db, cursor = get_db()
            cursor.execute(
                'INSERT INTO todo(description, deadline, completed, created_by)'
                'VALUES (%s, %s, %s, %s)',
                (description, deadline, False, g.user['id'])
            )
            db.commit()
            return redirect(url_for('todo.home'))
    return render_template('todo/create.html')


def get_todo(id):
    db, cursor = get_db()
    cursor.execute(
        'SELECT t.id, t.deadline, t.description, t.completed, t.created_at, t.created_by, u.username '
        'FROM todo t JOIN user u on t.created_by = u.id WHERE t.id = %s AND u.id = %s',
        (id, g.user['id'],)
    )
    todo = cursor.fetchone()
    if todo is None:
        abort(404, 'To-Do with id {0} doesn`t exist '.format(id))

    return todo


@bluePrint.route('/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update(id):
    todo = get_todo(id)
    if request.method == 'POST':
        description = request.form['description']
        deadline = request.form['deadline']
        completed = True if request.form.get('completed') == 'on' else False
        error = None
        if not description:
            error = 'Description is required'
        if error is not None:
            flash(error)
        else:
            db, cursor = get_db()
            cursor.execute(
                'UPDATE todo SET deadline = %s,  description = %s, completed = %s '
                'WHERE id = %s AND created_by = %s ',
                (deadline, description, completed, id, g.user['id'])
            )
            db.commit()
            return redirect(url_for('todo.home'))
    return render_template('todo/update.html', todo=todo)


@bluePrint.route('/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete(id):
    db, cursor = get_db()
    cursor.execute(
        'DELETE FROM todo WHERE id = %s AND created_by = %s ', (id, g.user['id'])
    )
    db.commit()
    return redirect(url_for('todo.home'))

