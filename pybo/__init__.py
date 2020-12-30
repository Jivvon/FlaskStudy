from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

"""
SQLAlchemy, Migrate 같은 db 객체를 create_app 함수 밖에서 생성하고
실제 초기화는 create_app 함수에서 수행하여 blueprint와 같은 다른 모듈이 db객체를 사용하지 못하도록 한다. 
"""

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    # blueprint
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    return app
