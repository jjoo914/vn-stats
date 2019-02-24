
"""
Stats-VN website
"""

from app import app
from app.modules.statics import BLUEPRINT as Statics
from app.modules.frontend.app import BLUEPRINT as Frontend


app.register_blueprint(Frontend)
app.register_blueprint(Statics, url_prefix='/statics')
