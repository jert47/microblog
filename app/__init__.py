from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)  # reads in cofiguration in config.py

from app import routes
