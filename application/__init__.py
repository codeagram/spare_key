from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
csrf = CSRFProtect(app)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProdConfig")

else:
    app.config.from_object("config.DevConfig")


db = SQLAlchemy(app)
migrate = Migrate(app, db)


with app.app_context():

    from .spare_key import SpareKeyBP
    app.register_blueprint(SpareKeyBP)

    db.create_all()
