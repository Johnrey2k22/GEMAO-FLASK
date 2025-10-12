from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'  # Change this in a real application

    from .auth.routes import auth_bp
    from .user.routes import user_bp
    from .cashier.routes import cashier_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(cashier_bp)

    return app
