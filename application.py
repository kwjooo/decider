from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello decider</h1>"


def create_app():
    return app
