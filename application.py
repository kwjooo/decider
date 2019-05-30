from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from resources.user import user_bp
from config import MariaDBConfig

app = Flask(__name__)
app.config.from_object(MariaDBConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.user import User
from models.category import Category
from models.grade import Grade
from models.group import Group
from models.restaurant import Restaurant
from models.vote import Vote
from models.category_preference import CategoryPreference
from models.today_restaurant import TodayRestaurant

app.register_blueprint(user_bp, url_prefix='/api/v1')


def create_app():
    return app
