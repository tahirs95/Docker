#!/usr/bin/env python3
from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()

def create_app(**config_overrides):
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')
    app.config.update(config_overrides)

    db.init_app(app)


    from counter.views import counter_app
    app.register_blueprint(counter_app)
    return app

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')