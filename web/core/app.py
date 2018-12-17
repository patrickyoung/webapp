from flask import Flask

def create_app(config_file=None):
    app = Flask(__name__)
    _regster_blueprints(app)
    return app

def _regster_blueprints(app):
    from web.blueprints import app1_bp
    app.register_blueprint(app1_bp)