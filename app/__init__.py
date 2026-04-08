import os
from typing import Optional

from flask import Flask

from app.cli import register_commands
from app.extensions import db
from config import config_by_name


def create_app(config_name: Optional[str] = None) -> Flask:
    app = Flask(__name__, template_folder="templates", static_folder="static")

    selected_config = config_name or os.getenv("FLASK_CONFIG", "development")
    app.config.from_object(config_by_name.get(selected_config, config_by_name["development"]))

    init_extensions(app)
    register_blueprints(app)
    register_commands(app)

    return app


def init_extensions(app: Flask) -> None:
    db.init_app(app)

    with app.app_context():
        from app import models  # noqa: F401


def register_blueprints(app: Flask) -> None:
    from app.auth import bp as auth_bp
    from app.courses import bp as courses_bp
    from app.main import bp as main_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(courses_bp)
