from flask import Blueprint

bp = Blueprint('predict',__name__)

from . import routes