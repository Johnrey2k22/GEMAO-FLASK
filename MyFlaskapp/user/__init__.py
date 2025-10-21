from flask import Blueprint

user_bp = Blueprint('user', __name__, template_folder='templates')

# Import the views module using the full module path to ensure the
# module is loaded and its route decorators are executed. Alias it to
# `user_views` so we don't shadow the `user_bp` Blueprint variable.
import MyFlaskapp.user.views as user_views
