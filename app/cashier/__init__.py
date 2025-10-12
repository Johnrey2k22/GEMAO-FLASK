from flask import Blueprint

cashier_bp = Blueprint('cashier', __name__)

from . import routes
