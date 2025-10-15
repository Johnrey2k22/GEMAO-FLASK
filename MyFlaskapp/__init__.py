from flask import Flask, render_template
import mysql.connector
from mysql.connector import Error

# Database configuration (moved from config.py)
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # default XAMPP MySQL password
    'port': 3306,
    # Use your existing XAMPP database
    'database': '2b_db'
}


def get_db_connection():
    """Create and return a MySQL connection using DB_CONFIG.

    Returns a mysql.connector connection or None on failure.
    """
    try:
        # If a database name is provided, connect to it directly.
        conn_args = dict(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            port=DB_CONFIG['port']
        )
        if DB_CONFIG.get('database'):
            conn_args['database'] = DB_CONFIG['database']

        connection = mysql.connector.connect(**conn_args)
        if connection.is_connected():
            print('Successfully connected to MySQL database')
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def init_db():
    """Initialize the database and required tables."""
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()

            # Use configured database name, create if missing (safe)
            db_name = DB_CONFIG.get('database') or 'gemao_db'
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`")
            cursor.execute(f"USE `{db_name}`")

            # Ensure the expected users table exists. Using IF NOT EXISTS is safe
            # if your `user_tb` already exists it will be left untouched.
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS user_tb (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(50) NOT NULL UNIQUE,
                    password VARCHAR(255) NOT NULL,
                    role VARCHAR(20) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            connection.commit()
            print("Database initialized successfully")
        except Error as e:
            print(f"Error initializing database: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("Database connection closed")


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mamamo123'

    # Initialize the database
    init_db()

    # Register blueprints
    from .authentication import auth_bp
    from .user import user_bp
    from .cashier import cashier_bp

    # Register authentication blueprint
    app.register_blueprint(auth_bp)

    try:
        app.register_blueprint(user_bp.bp)
    except Exception:
        try:
            app.register_blueprint(user_bp)
        except Exception:
            pass

    try:
        app.register_blueprint(cashier_bp.bp)
    except Exception:
        try:
            app.register_blueprint(cashier_bp)
        except Exception:
            pass

    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('errors/500.html'), 500

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)




