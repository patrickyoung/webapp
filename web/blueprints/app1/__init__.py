from flask import Blueprint

bp = Blueprint('registrar', __name__, template_folder='templates')

from . import manager, list