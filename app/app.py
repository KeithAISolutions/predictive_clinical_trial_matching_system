import os
from .config import ProductionConfig, DevelopmentConfig
from flask import Flask
from .main.routes import main_bp

config_map = {
    'DEVELOPMENT': DevelopmentConfig,
    'PRODUCTION': ProductionConfig 
}

def create_app(config_name=None):
    config = config_map.get(config_name or os.environ.get('APP_CONFIG'))
    app = Flask(__name__)
    app.config.from_object(config)
    app.secret_key = app.config['SECRET_KEY']
    app.register_blueprint(main_bp)
    return app
