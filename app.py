from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from models import db
from config import Config

#intialize flask extensions
bcrypt=Bcrypt()
jwt=JWTManager()
migrate =Migrate()


def create_app():
    
    app=Flask(__name__)

    #load config

    app.config.from_object(Config)

    #intialize extensions with app

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app,db)


    # Register blueprints (routes) - we'll add these next
    # from routes.auth import auth_bp
    # from routes.tasks import tasks_bp
    # app.register_blueprint(auth_bp)
    # app.register_blueprint(tasks_bp)

    return app

if __name__=='__main__':
    app=create_app()
    app.run(debug=True)
