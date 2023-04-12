import os
from .config import ProductionConfig, DevelopmentConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security
from flask_wtf import CSRFProtect
from .main.views import main_blueprint as main_bp

config_map = {
    'DEVELOPMENT': DevelopmentConfig,
    'PRODUCTION': ProductionConfig 
}

db = SQLAlchemy()
security = Security()
csrf = CSRFProtect()

def create_app(config_name=None):
    config = config_map.get(config_name or os.environ.get('APP_CONFIG'))
    app = Flask(__name__)
    app.config.from_object(config)
    app.secret_key = app.config['SECRET_KEY']
    db.init_app(app)
    security.init_app(app, db)
    csrf.init_app(app)
    app.register_blueprint(main_bp)

    return app
