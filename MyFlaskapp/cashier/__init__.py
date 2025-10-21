from flask import Blueprint

cashier_bp = Blueprint('cashier', __name__, template_folder='templates')

# Import the views module using the full module path so the route
# decorators run and register the routes on the `cashier_bp` Blueprint.
import MyFlaskapp.cashier.views as cashier_views
