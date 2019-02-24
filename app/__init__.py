
"""
Initialize Flask
"""

import os

from flask import Flask
from flask_compress import Compress
from dotenv import load_dotenv


load_dotenv()


class Config(object):
    """Flask configuration"""
    SEND_FILE_MAX_AGE_DEFAULT = 1296000
    SECRET_KEY = os.environ["SECRET_KEY"]


app = Flask(__name__)
app.config.from_object(Config())
app.jinja_env.lstrip_blocks = True
app.jinja_env.trim_blocks = True

# Compress settings
COMPRESS_MIMETYPES = [
    'text/html',
    'text/css',
    'text/xml',
    'application/json',
    'application/javascript'
]
COMPRESS_LEVEL = 6
COMPRESS_MIN_SIZE = 500
Compress(app)
