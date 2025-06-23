from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.config import Config


db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) #load configuration

    #initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    #register routes/controllers
    from server.controllers import register_controllers
    register_controllers(app)

    return app


#create the flask app
app = create_app()

#run the app
if __name__ == "__main__":
    app.run(debug=True)