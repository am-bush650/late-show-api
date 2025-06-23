from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.config import *


db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager


def create_app():
    app = Flask(__name__)
    app.config.from_object("server.config")



app = create_app()

if __name__ == "__main__":
    app.run(debug=True)