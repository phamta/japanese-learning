
import os

from flask import Flask, jsonify

from app.config import config_by_name
from app.extensions import (
    db,
    migrate,
    jwt,
    cors,
    limiter,
)


def create_app(config_name=None):
    # 1. Khởi tạo Flask application
    app = Flask(__name__)

    # 2. Đọc cấu hình
    config_name = config_name or os.getenv(
        "FLASK_CONFIG", "development"
    )

    app.config.from_object(config_by_name[config_name])

    # 3. Khởi tạo extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app)
    limiter.init_app(app)

    # 4. Health check API
    @app.get("/api/health")
    def health_check():
        return jsonify({
            "success": True,
            "message": "Japanese Learning API is running"
        }), 200

    @app.get("/")
    def root():
        return jsonify({
            "success": True,
            "message": "Hello from Japanese Learning API"
        }), 200

    # 5. Trả về application
    return app

# cmd to run the app: python -m flask --app wsgi run --debug