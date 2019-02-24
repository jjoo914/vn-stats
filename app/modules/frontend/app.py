
"""
Frontend module
"""

from app import app
from flask import Blueprint, jsonify


BLUEPRINT = Blueprint(
    "frontend",
    __name__,
)


@BLUEPRINT.route("/")
def index():
    """Show index page"""
    return app.send_static_file('index.html')
