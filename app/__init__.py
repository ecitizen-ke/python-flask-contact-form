from flask import Flask
from .main import main_bp


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "21e3367163225c129615869b0a84ffd2dc64177564df2062"

    # Register blueprints
    app.register_blueprint(main_bp)

    return app
