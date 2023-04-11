from flask import render_template
from .routes import main_bp

@main_bp.route('/about')
def about():
    return render_template('main/about.html')
