# app.py - main Flask app
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Auto Like System Running!'
