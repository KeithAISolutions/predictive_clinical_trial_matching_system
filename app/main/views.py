from flask import Blueprint

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/hello')
def hello():
    return "Hello, World!"
