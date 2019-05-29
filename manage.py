from application import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models.user import User
from models.category import Category
from models.grade import Grade
from models.group import Group
from models.restaurant import Restaurant
from models.vote import Vote
from models.category_preference import CategoryPreference
from models.today_restaurant import TodayRestaurant

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
