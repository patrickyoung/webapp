from flask import render_template
from . import bp

@bp.route('/list')
def list():
    return render_template('list.html')