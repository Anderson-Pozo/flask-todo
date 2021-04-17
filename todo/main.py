import os
from flask import Flask, render_template
from decouple import config


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='mykey',
        DATABASE_HOST=config('DB_HOST'),
        DATABASE_PASSWORD=config('DB_PASSWORD'),
        DATABASE_USER=config('DB_USER'),
        DATABASE=config('DB_NAME'),
    )

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bluePrint)

    from . import tasks
    app.register_blueprint(tasks.bluePrint)

    @app.errorhandler(404)
    def not_found(e):
        return render_template('status/404.html')

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('status/500.html')

    return app